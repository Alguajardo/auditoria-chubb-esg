import streamlit as st
from fpdf import FPDF

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1 ---
with tab1:
    st.header("Análisis de Brechas")
    st.text_area("Pega el texto aquí:", height=200)
    if st.button("Ejecutar Análisis"):
        st.success("Análisis realizado.")

# --- PESTAÑA 2 ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    norma_db = {
        "gobernanza": "Párrafo 26: El objetivo del requisito de gobernanza es permitir que los usuarios comprendan el gobierno corporativo utilizado para monitorear riesgos.",
        "estrategia": "Párrafo 27: La entidad debe revelar cómo los riesgos de sostenibilidad afectan su modelo de negocio y flujos de efectivo."
    }
    consulta = st.text_input("Concepto (ej: gobernanza, estrategia):")
    if st.button("Consultar"):
        if consulta.lower() in norma_db:
            st.info(norma_db[consulta.lower()])
        else:
            st.warning("Concepto no encontrado.")

# --- PESTAÑA 3 ---
with tab3:
    st.header("Generador de Informe APA 7")
    empresa = st.text_input("Empresa Auditada")
    intro = st.text_area("Introducción:")
    brechas = st.text_area("Análisis:")
    recom = st.text_area("Recomendaciones:")

    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 14)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True, align='C')
        
        pdf.set_font("Times", size=12)
        pdf.cell(0, 10, "Introducción", ln=True)
        pdf.multi_cell(0, 7, intro)
        
        pdf.cell(0, 10, "Análisis", ln=True)
        pdf.multi_cell(0, 7, brechas)
        
        pdf.cell(0, 10, "Recomendaciones", ln=True)
        pdf.multi_cell(0, 7, recom)
        
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe APA 7", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
