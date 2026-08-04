import sqlite3
import pandas as pd
from decimal import Decimal
import os

DB_NAME = 'nomina_data.db'

def get_connection():
    # check_same_thread=False is necessary for Streamlit since it uses multiple threads
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Company Config Settings
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS CompanyConfig (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            name TEXT,
            nit TEXT,
            prepared_by TEXT,
            logo BLOB
        )
    ''')
    
    # 2. Employees Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            doc_type TEXT,
            doc_num TEXT,
            salary DECIMAL(10, 2)
        )
    ''')
    
    # 3. History / Records Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id INTEGER,
            month TEXT,
            quincena INTEGER,
            type TEXT,
            incap_percent TEXT,
            start_date TEXT,
            end_date TEXT,
            days TEXT,
            value DECIMAL(12, 2),
            obs TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (emp_id) REFERENCES Employees(id) ON DELETE CASCADE
        )
    ''')
    
    # Initialize company config row if missing
    cursor.execute('INSERT OR IGNORE INTO CompanyConfig (id, name, nit, prepared_by) VALUES (1, "", "", "")')
    
    # Initialize basic employees based on original JS list if DB is empty
    cursor.execute('SELECT COUNT(*) as count FROM Employees')
    if cursor.fetchone()['count'] == 0:
        initial_emp = [
            ("Cristian David Ramirez Estrada", "C.C.", "1000747333", 1750905.00),
            ("David Coronado Cuadrado", "C.C.", "1015069712", 1950905.00),
            ("Jhon Alejandro Muñoz Legarda", "C.C.", "1040739221", 2100000.00),
            ("John Fredy Sanchez Zapata", "C.C.", "98659334", 1750905.00),
            ("Luis Rivas", "P.P.T.", "5052949", 1750905.00),
            ("Teófilo Ariza Gamboa", "C.C.", "79598483", 2250905.00),
            ("Juan Felipe Ramírez Meneses", "C.C.", "3414736", 1750905.00)
        ]
        cursor.executemany('INSERT INTO Employees (name, doc_type, doc_num, salary) VALUES (?, ?, ?, ?)', initial_emp)
        
    conn.commit()
    conn.close()

# --- COMPANY CONFIG METHODS ---
def get_company_config():
    conn = get_connection()
    config = conn.execute('SELECT * FROM CompanyConfig WHERE id = 1').fetchone()
    conn.close()
    return dict(config) if config else {}

def update_company_config(name, nit, prepared_by, logo=None):
    conn = get_connection()
    try:
        if logo is not None:
            conn.execute('UPDATE CompanyConfig SET name=?, nit=?, prepared_by=?, logo=? WHERE id=1', (name, nit, prepared_by, logo))
        else:
            conn.execute('UPDATE CompanyConfig SET name=?, nit=?, prepared_by=? WHERE id=1', (name, nit, prepared_by))
        conn.commit()
    finally:
        conn.close()

# --- EMPLOYEES METHODS ---
def get_employees():
    conn = get_connection()
    df = pd.read_sql_query('SELECT * FROM Employees', conn)
    conn.close()
    return df

def add_employee(name, doc_type, doc_num, salary):
    conn = get_connection()
    try:
        conn.execute('INSERT INTO Employees (name, doc_type, doc_num, salary) VALUES (?, ?, ?, ?)', (name, doc_type, doc_num, salary))
        conn.commit()
    finally:
        conn.close()

def delete_employee(emp_id):
    conn = get_connection()
    try:
        # Cascade delete is handled if PRAGMA foreign_keys = ON, but we explicitly delete to be safe
        conn.execute('DELETE FROM Records WHERE emp_id=?', (emp_id,))
        conn.execute('DELETE FROM Employees WHERE id=?', (emp_id,))
        conn.commit()
    finally:
        conn.close()

# --- RECORDS METHODS ---
def get_records(month, quincena):
    conn = get_connection()
    query = '''
    SELECT r.id, e.name, e.doc_type || ' ' || e.doc_num as doc, r.type, r.incap_percent, r.start_date, r.end_date, r.days, r.value, r.obs 
    FROM Records r
    JOIN Employees e ON r.emp_id = e.id
    WHERE r.month = ? AND r.quincena = ?
    ORDER BY r.created_at ASC
    '''
    df = pd.read_sql_query(query, conn, params=(month, quincena))
    conn.close()
    return df

def add_record(emp_id, month, quincena, rec_type, incap_percent, start_date, end_date, days, value, obs):
    conn = get_connection()
    try:
        conn.execute('''
            INSERT INTO Records (emp_id, month, quincena, type, incap_percent, start_date, end_date, days, value, obs)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (emp_id, month, quincena, rec_type, incap_percent, start_date, end_date, days, value, obs))
        conn.commit()
    finally:
        conn.close()

def delete_record(record_id):
    conn = get_connection()
    try:
        conn.execute('DELETE FROM Records WHERE id=?', (record_id,))
        conn.commit()
    finally:
        conn.close()

def get_history():
    conn = get_connection()
    query = 'SELECT DISTINCT month, quincena FROM Records ORDER BY month DESC, quincena DESC'
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

def delete_month_history(month):
    conn = get_connection()
    try:
        conn.execute('DELETE FROM Records WHERE month=?', (month,))
        conn.commit()
    finally:
        conn.close()
