import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import io

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# --- DEFINICIÓN DE PESTAÑAS (Esto debe ir ANTES de usar tab1, tab2, tab3) ---
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1 ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'])
    texto = st.text_area("O pega el texto aquí:", height=200)
    if st.button("Ejecutar Análisis"):
        st.success("Análisis técnico en curso...")

# --- PESTAÑA 2 ---
with tab2:
    st.header("Asistente Técnico ESG")
    pregunta = st.text_input("Consulta IFRS S1/S2:")
    if st.button("Consultar"):
        st.write("Procesando...")

# --- PESTAÑA 3 ---
with tab3:
    st.header("Generador de Informe Ejecutivo")
    empresa = st.text_input("Nombre de la Empresa")
    s1 = st.slider("Avance IFRS S1 (%)", 0, 100, 50)
    s2 = st.slider("Avance IFRS S2 (%)", 0, 100, 50)
    obs = st.text_area("Observaciones")
    
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True)
        
        # Gráfica
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(['S1', 'S2'], [s1, s2], color=['#2E86C1', '#C0392B'])
        plt.savefig("grafica.png")
        pdf.image("grafica.png", x=50, w=80)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe", pdf_bytes, "Informe.pdf", "application/pdf")
