import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la página en Streamlit
st.set_page_config(
    page_title="AMR SUITE | BAJO RELIEVE",
    page_icon="❖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Leemos el archivo index.html que creaste en el paso anterior
try:
    with open("index.html", "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Mostramos el contenido HTML
    components.html(html_code, height=900, scrolling=True)

except FileNotFoundError:
    st.error("Por favor, asegúrate de haber creado el archivo 'index.html' en tu repositorio de GitHub con el código de la aplicación.")
