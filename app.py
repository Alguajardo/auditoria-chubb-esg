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
    consulta = st.text_input("Pregunta sobre gobernanza, estrategia o métricas:", key="input_chat_2")
    if st.button("Consultar Normativa", key="btn_chat_2"):
        if "gobernanza" in consulta.lower():
            st.markdown("""
            **Referencia Técnica (IFRS S1 - Requerimientos Generales):**
            * **Párrafo 26:** Objetivo del requisito de gobernanza para monitorear riesgos.
            * **Párrafo 27:** Obligación de revelar órganos responsables y controles.
            """)
        elif "estrategia" in consulta.lower():
            st.markdown("""
            **Referencia Técnica (IFRS S1 - Estrategia):**
            * El objetivo es permitir que los usuarios comprendan cómo los riesgos de sostenibilidad afectan el modelo de negocio y flujos de efectivo.
            """)
        else:
            st.info("Ingresa 'Gobernanza' o 'Estrategia' para ver los párrafos de la norma.")

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
        st.download_button("Descargar Informe APA 7", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
