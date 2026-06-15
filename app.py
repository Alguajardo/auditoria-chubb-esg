import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import io

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1 ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'])
    texto = st.text_area("O pega el texto aquí para análisis inmediato:", height=200)
    if st.button("Ejecutar Análisis"):
        st.success("Análisis técnico en curso...")

# --- PESTAÑA 2 ---
with tab2:
    st.header("Asistente Técnico ESG")
    st.write("Consulta pilares IFRS S1 y S2.")
    consulta = st.text_input("Ingresa tu consulta:")
    if st.button("Consultar"):
        st.markdown("""
        **Análisis IFRS S1/S2:**
        1. **Gobernanza:** Monitoreo de riesgos.
        2. **Estrategia:** Impacto financiero climático.
        3. **Gestión de Riesgos:** Identificación y mitigación.
        4. **Métricas:** Revelación de indicadores (GEI).
        """)

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
        pdf.cell(0, 10, f"Informe de Auditoria: {empresa}", ln=True, align='C')
        
        # Gráfica
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.bar(['S1', 'S2'], [s1, s2], color=['#2E86C1', '#C0392B'])
        plt.savefig("grafica.png")
        pdf.image("grafica.png", x=50, w=80)
        
        pdf.set_font("Arial", size=12)
        pdf.ln(85)
        pdf.multi_cell(0, 10, f"Resumen:\nS1: {s1}%\nS2: {s2}%\n\nObservaciones:\n{obs}")
        
        # --- SOLUCIÓN: Convertir explícitamente a bytes ---
        pdf_output = pdf.output()
        pdf_bytes = bytes(pdf_output) 
        
        st.download_button(
            label="Descargar Informe PDF",
            data=pdf_bytes,
            file_name="Informe_Auditoria.pdf",
            mime="application/pdf"
        )
