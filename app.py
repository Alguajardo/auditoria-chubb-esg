import streamlit as st
from fpdf import FPDF
import os

st.title("Generador de Reporte IFRS S1/S2")

# --- Formulario de Entrada ---
st.sidebar.header("Datos de Auditoría")
empresa = st.sidebar.text_input("Nombre de la Empresa")
ejecutivo = st.sidebar.text_input("Consultor a cargo", "Alberto Guajardo")
brecha_s1 = st.sidebar.slider("Nivel de cumplimiento IFRS S1 (%)", 0, 100, 50)
brecha_s2 = st.sidebar.slider("Nivel de cumplimiento IFRS S2 (%)", 0, 100, 50)
observaciones = st.text_area("Observaciones y Recomendaciones Técnicas")

if st.button("Generar Informe PDF"):
    temp_file = "Reporte_IFRS.pdf"
    
    # --- Estructura del PDF ---
    pdf = FPDF()
    pdf.add_page()
    
    # Encabezado
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INFORME DE ANALISIS DE BRECHAS IFRS", ln=True, align='C')
    pdf.ln(10)
    
    # Cuerpo
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, f"Empresa: {empresa}", ln=True)
    pdf.cell(0, 10, f"Consultor: {ejecutivo}", ln=True)
    pdf.ln(5)
    pdf.cell(0, 10, f"Avance IFRS S1: {brecha_s1}%", ln=True)
    pdf.cell(0, 10, f"Avance IFRS S2: {brecha_s2}%", ln=True)
    pdf.ln(10)
    pdf.cell(0, 10, "Observaciones:", ln=True)
    pdf.multi_cell(0, 10, observaciones)
    
    # Salida
    pdf.output(temp_file)
    
    with open(temp_file, "rb") as f:
        st.download_button("Descargar Informe IFRS", f, "Informe_IFRS.pdf", "application/pdf")
