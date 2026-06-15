import streamlit as st
from fpdf import FPDF

# Configuración de la página
st.set_page_config(page_title="Auditoría ESG", layout="centered")

st.title("Plataforma de Auditoría ESG")
st.write("Bienvenido, Alberto. Esta herramienta permite generar informes de auditoría.")

if st.button("Generar Informe"):
    # Creamos el PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INFORME DE AUDITORIA ESG", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, "Informe generado exitosamente.", ln=True)
    
    # Generar bytes (fpdf2)
    pdf_bytes = pdf.output(dest='S')
    
    # Botón de descarga
    st.download_button(
        label="Descargar PDF",
        data=pdf_bytes,
        file_name="Auditoria_ESG.pdf",
        mime="application/pdf"
    )
