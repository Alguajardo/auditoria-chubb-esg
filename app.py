import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Auditoría ESG Pro", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {"Introducción": "", "Gobernanza": "", "Estrategia": "", "Riesgos y Oportunidades": "", "Métricas": "", "Conclusiones": "", "Recomendaciones": ""}

tab1, tab2, tab3 = st.tabs(["📊 Análisis y Dashboard", "🤖 Chatbot ESG", "📄 Informe Tipo Australis"])

# Pestaña 1: Análisis (Dashboard)
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    if st.button("Ejecutar Análisis"):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        st.bar_chart(pd.DataFrame({"Valor": [20, 50, 30]}, index=["Gobernanza", "Estrategia", "Métricas"]))
        
        st.session_state.informe_data = {
            "Introducción": "Este análisis ESG aplica una convergencia estratégica de estándares internacionales a la operativa, vinculando resiliencia con resultados económicos.",
            "Gobernanza": "Soporte bajo Código de Ética. Comité de Ética activo y certificación ISO 45001 mantenida.",
            "Estrategia": "Integración vertical y alimentación remota. Materialidad enfocada en trazabilidad y resiliencia operativa.",
            "Riesgos y Oportunidades": "Dependencia FFDR y riesgos climáticos. Oportunidades en bioseguridad e innovación tecnológica.",
            "Métricas": "Cosecha 2024: 48.146 tons WFE. Desperdicio < 1%. Falta cuantificación Scope 3.",
            "Conclusiones": "Madurez en gobernanza. Existe brecha en cuantificación financiera de riesgos climáticos (IFRS S2).",
            "Recomendaciones": "Vincular riesgos climáticos con el Estado de Resultados y fortalecer el aseguramiento continuo."
        }
        st.success("Análisis realizado: Datos listos para el informe.")

# Pestaña 3: Generador de Informe (Tipo Australis)
with tab3:
    st.header("Generador de Informe ESG - Formato Corporativo")
    empresa = st.text_input("Nombre de la Empresa", "Australis Seafoods S.A.")
    
    # Editor visual
    datos = st.session_state.informe_data
    for k in datos:
        datos[k] = st.text_area(f"{k}:", value=datos[k])
    
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        # Header Corporativo
        pdf.set_font("Times", 'B', 18)
        pdf.cell(0, 15, f"INFORME ESG: {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        for titulo, contenido in datos.items():
            pdf.set_font("Times", 'B', 14)
            pdf.cell(0, 10, titulo, ln=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 8, contenido)
            pdf.ln(5)
            
        pdf.ln(20)
        pdf.set_font("Times", 'I', 10)
        pdf.cell(0, 10, "Auditoría ejecutada mediante Metodología de Filtrado Atómico", ln=True)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG_Corporativo.pdf", "application/pdf")
