import streamlit as st
import pandas as pd
import datetime
import calendar
import database as db
import logic

# Setup initial configurations
st.set_page_config(page_title="AMR NÓMINA", page_icon="🏢", layout="wide")

# Initialize DB
db.init_db()

def to_month_name(date_str):
    if not date_str: return ""
    try:
        y, m = date_str.split('-')
        month_name = calendar.month_name[int(m)]
        # Translate to Spanish
        es_months = {
            "January": "ENERO", "February": "FEBRERO", "March": "MARZO", "April": "ABRIL",
            "May": "MAYO", "June": "JUNIO", "July": "JULIO", "August": "AGOSTO",
            "September": "SEPTIEMBRE", "October": "OCTUBRE", "November": "NOVIEMBRE", "December": "DICIEMBRE"
        }
        return es_months.get(month_name, month_name).upper()
    except Exception:
        return ""

def main():
    # Sidebar
    with st.sidebar:
        st.markdown("<h2 style='text-align: center; color: #fbbf24; background-color: #0f172a; padding: 10px; border-radius: 5px; font-size: 16px;'>AMR SUITE NÓMINA PARA SEGURIDAD SOCIAL</h2>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        
        st.markdown("### 1. Identificación")
        config = db.get_company_config()
        co_name = st.text_input("NOMBRE EMPRESA", value=config.get('name', ''))
        co_nit = st.text_input("NIT", value=config.get('nit', ''))
        prep_by = st.text_input("ELABORADO POR...", value=config.get('prepared_by', ''))
        logo_file = st.file_uploader("Subir Logo", type=['png', 'jpg', 'jpeg'])
        if st.button("Guardar Identificación", use_container_width=True):
            logo_bytes = logo_file.read() if logo_file else config.get('logo')
            db.update_company_config(co_name, co_nit, prep_by, logo_bytes)
            st.success("Configuración guardada")
        
        st.divider()
        st.markdown("### 2. Registro de Novedad")
        col1, col2 = st.columns([2, 1])
        with col1:
            current_month = datetime.date.today().strftime('%Y-%m')
            report_month = st.text_input("Mes (YYYY-MM)", value=current_month)
        with col2:
            q_select = st.selectbox("Quincena", [1, 2])
            
        employees_df = db.get_employees()
        emp_options = {row['name']: row['id'] for _, row in employees_df.iterrows()}
        emp_selected = st.selectbox("Trabajador", options=["Seleccionar Trabajador..."] + list(emp_options.keys()))
        
        if emp_selected != "Seleccionar Trabajador...":
            emp_data = employees_df[employees_df['name'] == emp_selected].iloc[0]
            st.info(f"**Documento**: {emp_data['doc_type']} {emp_data['doc_num']}\n\n**Salario**: {logic.format_currency(emp_data['salary'])}")
            emp_id = emp_data['id']
        else:
            emp_id = None
            
        nov_types = [
            "Aumento Salarial", "Comisión", "Horas extras - Recargos", 
            "Incapacidad por Accidente Laboral ARL", "Incapacidad por enfermedad General EPS", 
            "Ingreso Laboral", "Licencia Maternidad", "Permiso NO Remunerado", 
            "Permiso Remunerado", "Retiro Laboral", "Vacaciones", "Licencia de Paternidad"
        ]
        nov_type = st.selectbox("Tipo de Novedad", [""] + nov_types)
        incap_percent = st.text_input("% INCAP")
        
        col3, col4 = st.columns(2)
        with col3: date_start = st.date_input("Inicio", value=None)
        with col4: date_end = st.date_input("Fin", value=None)
        
        col5, col6 = st.columns(2)
        with col5: d_days = st.text_input("Días")
        with col6: d_val = st.text_input("Valor $")
        
        d_obs = st.text_area("Observaciones...")
        
        if st.button("AGREGAR NOVEDAD", type="primary", use_container_width=True):
            if not emp_id:
                st.error("Seleccione un trabajador")
            else:
                db.add_record(
                    emp_id=emp_id,
                    month=report_month,
                    quincena=q_select,
                    rec_type=nov_type if nov_type else "No aplica",
                    incap_percent=incap_percent if incap_percent else "No aplica",
                    start_date=date_start.strftime("%Y-%m-%d") if date_start else "No aplica",
                    end_date=date_end.strftime("%Y-%m-%d") if date_end else "No aplica",
                    days=d_days if d_days else "No aplica",
                    value=float(d_val) if d_val else None,
                    obs=d_obs if d_obs else "No aplica"
                )
                st.success("Novedad agregada")
                st.rerun()

        st.divider()
        st.markdown("### 3. Historial de Reportes")
        history_df = db.get_history()
        hist_months = history_df['month'].unique()
        for hm in hist_months:
            with st.expander(f"Mes: {hm}"):
                qs = history_df[history_df['month'] == hm]['quincena'].tolist()
                st.write(f"Quincenas con datos: {', '.join(map(str, qs))}")
                if st.button(f"Borrar mes {hm}", key=f"del_hm_{hm}"):
                    db.delete_month_history(hm)
                    st.rerun()
                    
        st.divider()
        st.markdown("### 4. Gestión de Personal")
        with st.expander("Agregar / Ver Trabajadores"):
            new_emp_name = st.text_input("Nombre Completo")
            col7, col8 = st.columns([1, 2])
            with col7: new_emp_type = st.selectbox("Tipo", ["CC", "CE", "PPT", "PEP", "TI"])
            with col8: new_emp_doc = st.text_input("Número")
            new_emp_sal = st.number_input("Salario Base", step=1000.0)
            if st.button("Guardar Trabajador", use_container_width=True):
                if new_emp_name and new_emp_doc:
                    db.add_employee(new_emp_name, new_emp_type, new_emp_doc, new_emp_sal)
                    st.success("Trabajador agregado")
                    st.rerun()
                else:
                    st.error("Nombre y Número son requeridos")
            
            st.markdown("##### Lista Actual")
            for _, emp in employees_df.iterrows():
                cc1, cc2 = st.columns([4, 1])
                cc1.write(emp['name'])
                if cc2.button("🗑️", key=f"del_emp_{emp['id']}"):
                    db.delete_employee(emp['id'])
                    st.rerun()

    # Main Area
    col_download_1, col_download_2, col_download_3 = st.columns([6, 2, 2])
    
    df_records = db.get_records(report_month, q_select)
    config = db.get_company_config()
    month_text = to_month_name(report_month)
    period_text = f"{q_select}ª QUINCENA DE {month_text}" if month_text else f"{q_select}ª QUINCENA"
    
    with col_download_2:
        if st.button("📊 Excel", use_container_width=True):
            excel_data = logic.generate_excel(df_records)
            st.download_button(
                label="Descargar Excel",
                data=excel_data,
                file_name=f"Reporte_AMR_{report_month}_Q{q_select}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
            
    with col_download_3:
        if st.button("📄 DESCARGAR PDF", use_container_width=True):
            pdf_data = logic.generate_pdf(df_records, config, period_text)
            st.download_button(
                label="Descargar PDF",
                data=pdf_data,
                file_name=f"Reporte_AMR_{report_month}_Q{q_select}.pdf",
                mime="application/pdf",
                use_container_width=True
            )

    st.markdown("---")
    
    # Render Report Dashboard View
    col_h1, col_h2 = st.columns([1, 1])
    with col_h1:
        if config.get('logo'):
            st.image(config['logo'], width=200)
    with col_h2:
        st.markdown(f"<h2 style='text-align: right; color: #6366f1;'>NOVEDADES DE NÓMINA - SEGURIDAD SOCIAL</h2>", unsafe_allow_html=True)
        st.markdown(f"<h4 style='text-align: right; color: #475569;'>{period_text}</h4>", unsafe_allow_html=True)
        
    st.markdown(f"<h1 style='color: #1e293b; margin-bottom: 0px;'>{config.get('name', '---').upper()}</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='color: #64748b; margin-top: 0px;'>NIT: {config.get('nit', '---')}</h4>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if not df_records.empty:
        disp_df = df_records.copy()
        
        # We manually render the rows for exact layout control as the original app
        for idx, row in disp_df.iterrows():
            with st.container():
                c1, c2, c3, c4, c5, c6, c7, c8, c9, c10 = st.columns([3.5, 2.5, 3.5, 1, 2, 2, 1, 2.5, 5, 1])
                if idx == 0:
                    c1.markdown("**TRABAJADOR**")
                    c2.markdown("**DOCUMENTO**")
                    c3.markdown("**NOVEDAD**")
                    c4.markdown("**%**")
                    c5.markdown("**INICIO**")
                    c6.markdown("**FIN**")
                    c7.markdown("**DÍAS**")
                    c8.markdown("**VALOR**")
                    c9.markdown("**OBSERVACIONES**")
                    c10.markdown("**ACC**")
                
                c1.write(f"<b>{row['name']}</b>", unsafe_allow_html=True)
                c2.write(row['doc'])
                color_type = "#dc2626" if row['type'] == "No aplica" else "#1e293b"
                c3.markdown(f"<span style='color: {color_type}; font-weight: bold;'>{row['type']}</span>", unsafe_allow_html=True)
                c4.write(row['incap_percent'])
                c5.write(row['start_date'])
                c6.write(row['end_date'])
                c7.write(row['days'])
                
                val_formatted = logic.format_currency(row['value'])
                c8.markdown(f"<span style='color: #4338ca; font-weight: bold;'>{val_formatted}</span>", unsafe_allow_html=True)
                c9.write(row['obs'])
                
                if c10.button("🗑️", key=f"del_rec_{row['id']}"):
                    db.delete_record(row['id'])
                    st.rerun()
            st.divider()
    else:
        st.info("No hay registros para este periodo.")
        
    st.markdown(f"<p style='color: #94a3b8; font-size: 12px; font-weight: bold; margin-top: 40px;'>Elaborado por: <span style='color: #0f172a; font-style: italic;'>{config.get('prepared_by', '---')}</span><span style='float: right;'>AMR Consultoría © 2026</span></p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
