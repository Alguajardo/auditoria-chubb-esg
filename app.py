import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1 ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'], key="uploader_1")
    texto = st.text_area("O pega el texto aquí:", height=200, key="texto_analisis")
    if st.button("Ejecutar Análisis", key="btn_analisis"):
        st.success("Análisis técnico en curso...")

# --- PESTAÑA 2 ---
with tab2:
    st.header("Asistente Técnico ESG")
    consulta = st.text_input("Consulta IFRS S1/S2:", key="input_chatbot")
    if st.button("Consultar Normativa", key="btn_chatbot"):
        st.markdown("""
        **Pilares IFRS S1/S2:** 1. Gobernanza | 2. Estrategia | 3. Gestión de Riesgos | 4. Métricas.
        """)

# --- PESTAÑA 3 ---
with tab3:
    st.header("Generador de Informe Técnico")
    empresa = st.text_input("Empresa Auditada", key="empresa_nombre")
    brechas = st.text_area("Brechas detectadas:", "Ej: Párrafo 12 - Falta de revelación.")
    
    col1, col2 = st.columns(2)
    impacto = col1.number_input("Impacto Financiero (USD)", value=0, key="impacto_val")
    probabilidad = col2.slider("Probabilidad de Materialidad (%)", 0, 100, key="prob_val")
    
    recomendaciones = st.text_area("Recomendaciones Estratégicas:")

    # Botón único con key distinta
    if st.button("Generar Informe PDF Final", key="btn_pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Informe de Auditoría: {empresa}", ln=True, align='C')
        
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Conectividad estimada: ${impacto * (probabilidad/100):,.2f}", ln=True)
        pdf.multi_cell(0, 10, f"Brechas:\n{brechas}\n\nRecomendaciones:\n{recomendaciones}")
        
        # Generar bytes
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_Auditoria.pdf", "application/pdf")
