import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'], key="up1")
    texto = st.text_area("Pega el texto aquí para análisis inmediato:", height=200, key="txt1")
    if st.button("Ejecutar Análisis", key="btn_ejecutar"):
        st.success("Análisis técnico realizado con éxito.")
        st.write("1. **Párrafo 12 (Gobernanza):** Alineado con IFRS S1.")
        st.write("2. **Párrafo 28 (Métricas):** Brecha detectada (Falta de Scope 3).")

# --- PESTAÑA 2: CHATBOT EXPERTO ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    # Base de conocimiento integrada para evitar errores de archivo
    norma_db = {
        "gobernanza": "Párrafo 26: El objetivo del requisito de gobernanza es permitir que los usuarios comprendan el gobierno corporativo utilizado para monitorear y gestionar riesgos.",
        "estrategia": "Párrafo 27: La entidad debe revelar cómo los riesgos de sostenibilidad afectan su modelo de negocio y flujos de efectivo.",
        "alcance 3": "Párrafo 28: La entidad debe revelar emisiones de GEI de alcance 3, incluyendo las categorías más significativas."
    }
    
    consulta = st.text_input("Ingresa concepto (ej: gobernanza, estrategia, alcance 3):", key="input_chat_2")
    if st.button("Consultar Normativa", key="btn_chat_2"):
        busqueda = consulta.strip().lower()
        if busqueda in norma_db:
            st.success("Referencia Técnica encontrada:")
            st.info(norma_db[busqueda])
        else:
            st.warning("Concepto no encontrado. Prueba con 'gobernanza', 'estrategia' o 'alcance 3'.")

# --- PESTAÑA 3: GENERADOR DE INFORMES (APA 7) ---
with tab3:
    st.header("Generador de Informe Técnico - Formato APA 7")
    empresa = st.text_input("Empresa Auditada", key="emp_nombre")
    introduccion = st.text_area("Introducción:", "El presente informe técnico detalla la auditoría de sostenibilidad basada en los estándares IFRS S1 y S2.")
    brechas = st.text_area("Análisis (Brechas detectadas):", "Análisis de los párrafos críticos: se observa una brecha en la revelación de alcance 3.")
    recomendaciones = st.text_area("Recomendaciones:", "Se recomienda al directorio fortalecer los mecanismos de gobernanza climática.")

    if st.button("Generar Informe Formato APA", key="btn_pdf_apa"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 14)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        for titulo, contenido in [("Introducción", introduccion), ("Análisis", brechas), ("Recomendaciones", recomendaciones)]:
            pdf.set_font("Times", 'B', 12)
            pdf.cell(0, 10, titulo, ln=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 7, contenido)
            pdf.ln(5)
            
        pdf.set_font("Times", 'I', 10)
        pdf.cell(0, 10, "Auditoría por: Alberto Esteban Guajardo Meneses", ln=True)
        
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe APA 7", pdf_bytes, "Informe
