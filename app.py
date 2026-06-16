import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Auditoría ESG Pro", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicialización segura de estado
if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {}
if 'resumen_dashboard' not in st.session_state:
    st.session_state.resumen_dashboard = {}

tab1, tab2, tab3 = st.tabs(["📊 Análisis y Dashboard", "🤖 Chatbot ESG", "📄 Informe Tipo Australis"])

# Pestaña 1: Análisis
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    if st.button("Ejecutar Análisis"):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        st.session_state.resumen_dashboard = {"Gobernanza": "OK", "Estrategia": "Brecha", "Riesgos": "OK", "Métricas": "Crítico"}
        st.session_state.informe_data = {
            "Introducción": "Análisis ESG con enfoque en conectividad financiera.",
            "Gobernanza": "Cumple Párrafo 26; sistema de ética sólido.",
            "Estrategia": "Falta horizonte temporal de 3 años (Párrafo 27).",
            "Riesgos y Oportunidades": "Identificados riesgos climáticos; falta cuantificación.",
            "Métricas": "No se reporta alcance 3 (Párrafo 28).",
            "Conclusiones": "Madurez operativa con brechas en reporte IFRS S2.",
            "Recomendaciones": "Vincular riesgos con el Estado de Resultados."
        }
        st.success("Análisis realizado correctamente.")

# Pestaña 3: Generador de Informe
with tab3:
    st.header("Generador de Informe ESG")
    empresa = st.text_input("Empresa", "Australis Seafoods S.A.")
    
    if st.button("Generar Informe PDF"):
        # Verificación para evitar el AttributeError
        if not st.session_state.resumen_dashboard:
            st.warning("Por favor, ejecuta primero el análisis en la Pestaña 1.")
        else:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Times", 'B', 18)
            pdf.cell(0, 15, f"INFORME ESG: {empresa}", ln=True, align='C')
            
            pdf.set_font("Times", 'B', 14)
            pdf.cell(0, 10, "Resumen de Brechas (Dashboard)", ln=True)
            pdf.set_font("Times", size=12)
            
            for k, v in st.session_state.resumen_dashboard.items():
                pdf.cell(0, 8, f"- {k}: {v}", ln=True)
            pdf.ln(5)
            
            for titulo, contenido in st.session_state.informe_data.items():
                pdf.set_font("Times", 'B', 14)
                pdf.cell(0, 10, titulo, ln=True)
                pdf.set_font("Times", size=12)
                pdf.multi_cell(0, 8, contenido)
                pdf.ln(2)
                
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG_Final.pdf", "application/pdf")
