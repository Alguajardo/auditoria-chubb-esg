import streamlit as st
from fpdf import FPDF
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicializar estado para compartir datos entre pestañas
if 'resultados_analisis' not in st.session_state:
    st.session_state.resultados_analisis = {
        "Gobernanza": "Pendiente de análisis",
        "Estrategia": "Pendiente de análisis",
        "Riesgos": "Pendiente de análisis",
        "Metricas": "Pendiente de análisis",
        "Conectividad": "Pendiente de análisis",
        "Conclusiones": "Pendiente de análisis",
        "Recomendaciones": "Pendiente de análisis"
    }

tab1, tab2, tab3 = st.tabs(["📊 Análisis por Pilares", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria", type=['pdf', 'txt'])
    if st.button("Ejecutar Análisis"):
        # Simulamos el análisis técnico
        st.session_state.resultados_analisis = {
            "Gobernanza": "Cumple Párrafo 26; el comité de ética está activo.",
            "Estrategia": "Brecha: Falta horizonte temporal de 3 años (Párrafo 27).",
            "Riesgos": "Identificados riesgos climáticos, pero falta cuantificación financiera.",
            "Metricas": "Crítico: No se reporta alcance 3 (Párrafo 28).",
            "Conectividad": "Débil vínculo entre riesgos climáticos y estados financieros.",
            "Conclusiones": "Madurez en gobernanza pero requiere cuantificación financiera.",
            "Recomendaciones": "Vincular riesgos climáticos con el Estado de Resultados."
        }
        st.success("Análisis realizado. Datos cargados en el generador de informes.")

# --- PESTAÑA 2: CHATBOT ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    consulta = st.text_input("Consulta normativa:")
    if st.button("Consultar"):
        st.info("Párrafo 26-28: La entidad debe revelar riesgos y oportunidades de sostenibilidad.")

# --- PESTAÑA 3: GENERADOR DE INFORMES ---
with tab3:
    st.header("Generador de Informe Técnico")
    empresa = st.text_input("Empresa", "Australis Seafoods S.A.")
    
    # Mostrar brechas actuales
    st.subheader("Resumen de Brechas Detectadas")
    res = st.session_state.resultados_analisis
    for k, v in res.items():
        st.write(f"**{k}:** {v}")
        
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 16)
        pdf.cell(0, 10, f"Informe ESG: {empresa}", ln=True, align='C')
        pdf.set_font("Times", size=12)
        
        for k, v in res.items():
            pdf.ln(5)
            pdf.set_font("Times", 'B', 12)
            pdf.cell(0, 10, k, ln=True)
            pdf.set_font("Times", size=11)
            pdf.multi_cell(0, 7, v)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
