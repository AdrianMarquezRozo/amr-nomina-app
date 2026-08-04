import pandas as pd
from io import BytesIO
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.units import mm
import datetime

def format_currency(value):
    try:
        if value is None or str(value).strip() == "" or str(value).strip() == "No aplica" or pd.isna(value):
            return "No aplica"
        return f"$ {float(value):,.0f}".replace(",", ".")
    except ValueError:
        return value

def generate_excel(df_records):
    """
    Generates an Excel payload from the records DataFrame.
    """
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        disp_df = df_records.copy()
        disp_df.drop(columns=['id'], inplace=True, errors='ignore')
        disp_df['value'] = disp_df['value'].apply(format_currency)
        disp_df.columns = ['TRABAJADOR', 'DOCUMENTO', 'NOVEDAD', '%', 'INICIO', 'FIN', 'DÍAS', 'VALOR', 'OBSERVACIONES']
        disp_df.to_excel(writer, index=False, sheet_name='Novedades')
    return output.getvalue()

def generate_pdf(df_records, company_config, period_text):
    """
    Generates a PDF using reportlab to closely match the original styling.
    """
    output = BytesIO()
    doc = SimpleDocTemplate(
        output,
        pagesize=landscape(A4),
        rightMargin=15*mm, leftMargin=15*mm,
        topMargin=15*mm, bottomMargin=15*mm
    )
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Heading1'],
        textColor=colors.HexColor('#6366f1'),
        alignment=2,
        fontSize=14,
        fontName='Helvetica-Bold'
    )
    period_style = ParagraphStyle(
        'PeriodStyle',
        parent=styles['Normal'],
        textColor=colors.HexColor('#334155'),
        alignment=2,
        fontSize=10,
        fontName='Helvetica-Bold'
    )
    co_style = ParagraphStyle(
        'CoStyle',
        parent=styles['Heading2'],
        textColor=colors.HexColor('#1e293b'),
        fontSize=18,
        fontName='Helvetica-Bold'
    )
    nit_style = ParagraphStyle(
        'NitStyle',
        parent=styles['Normal'],
        textColor=colors.HexColor('#64748b'),
        fontSize=10,
        fontName='Helvetica-Bold'
    )
    
    header_data = []
    title_flowables = [
        Paragraph("NOVEDADES DE NÓMINA - SEGURIDAD SOCIAL", title_style),
        Spacer(1, 3),
        Paragraph(period_text.upper(), period_style)
    ]
    
    if company_config.get('logo'):
        logo_img = BytesIO(company_config['logo'])
        img = Image(logo_img, width=45*mm, height=15*mm, kind='proportional')
        header_data.append([img, title_flowables])
    else:
        header_data.append(["", title_flowables])
        
    header_table = Table(header_data, colWidths=[60*mm, 207*mm])
    header_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('ALIGN', (1,0), (1,0), 'RIGHT')
    ]))
    
    elements.append(header_table)
    elements.append(Spacer(1, 10))
    
    elements.append(Paragraph(company_config.get('name', '---').upper(), co_style))
    elements.append(Paragraph(f"NIT: {company_config.get('nit', '---')}", nit_style))
    elements.append(Spacer(1, 15))
    
    table_data = [['TRABAJADOR', 'DOCUMENTO', 'NOVEDAD', '%', 'INICIO', 'FIN', 'DÍAS', 'VALOR', 'OBSERVACIONES']]
    for _, row in df_records.iterrows():
        table_data.append([
            row['name'],
            row['doc'],
            row['type'],
            row['incap_percent'],
            row['start_date'],
            row['end_date'],
            str(row['days']),
            format_currency(row['value']),
            row['obs']
        ])
    
    col_widths = [45*mm, 25*mm, 35*mm, 15*mm, 20*mm, 20*mm, 15*mm, 30*mm, 62*mm]
    
    if df_records.empty:
        table_data.append(["No hay registros para este periodo", "", "", "", "", "", "", "", ""])
        t = Table(table_data, colWidths=col_widths)
        t_style = TableStyle([
            ('SPAN',(0,1),(-1,1)),
            ('ALIGN', (0,1), (-1,1), 'CENTER')
        ])
    else:
        t = Table(table_data, colWidths=col_widths)
        t_style = TableStyle([])
    
    t_style.add('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0f172a'))
    t_style.add('TEXTCOLOR', (0,0), (-1,0), colors.white)
    t_style.add('ALIGN', (0,0), (-1,0), 'CENTER')
    t_style.add('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold')
    t_style.add('FONTSIZE', (0,0), (-1,0), 8)
    t_style.add('BOTTOMPADDING', (0,0), (-1,0), 6)
    t_style.add('TOPPADDING', (0,0), (-1,0), 6)
    t_style.add('GRID', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1'))
    
    t_style.add('ALIGN', (0,1), (0,-1), 'LEFT')
    t_style.add('ALIGN', (1,1), (6,-1), 'CENTER')
    t_style.add('ALIGN', (7,1), (7,-1), 'RIGHT')
    t_style.add('FONTSIZE', (0,1), (-1,-1), 8)
    t_style.add('VALIGN', (0,0), (-1,-1), 'MIDDLE')
    
    for i, row in enumerate(table_data[1:], start=1):
        if len(row) > 2 and row[2] == "No aplica":
            t_style.add('TEXTCOLOR', (2,i), (2,i), colors.HexColor('#dc2626'))
            t_style.add('FONTNAME', (2,i), (2,i), 'Helvetica-Bold')
            
    t.setStyle(t_style)
    elements.append(t)
    
    elements.append(Spacer(1, 20))
    
    prepared_by = company_config.get('prepared_by', '---')
    
    footer_data = [
        [
            Paragraph(f"Elaborado por: <i>{prepared_by}</i>", ParagraphStyle('Footer1', fontSize=8, textColor=colors.HexColor('#94a3b8'))),
            Paragraph("AMR Consultoría © 2026", ParagraphStyle('Footer2', fontSize=8, textColor=colors.HexColor('#94a3b8'), alignment=2))
        ]
    ]
    
    footer_table = Table(footer_data, colWidths=[133*mm, 134*mm])
    footer_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,0), 'TOP'),
        ('LINEABOVE', (0,0), (-1,0), 1, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,0), 8)
    ]))
    
    elements.append(footer_table)
    
    doc.build(elements)
    return output.getvalue()
