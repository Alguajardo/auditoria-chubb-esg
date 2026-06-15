import streamlit as st
from fpdf import FPDF
import io

st.title("Plataforma de Auditoría ESG")

if st.button("Generar Informe"):
    # 1. Crear el objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INFORME DE AUDITORIA ESG", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, "Informe generado correctamente con fpdf2.", ln=True)
    
    # 2. Guardar en un buffer de memoria (BytesIO)
    # FPDF.output() devuelve bytes directamente en fpdf2 si no especificas ruta
    pdf_bytes = pdf.output()
    buffer = io.BytesIO(pdf_bytes)
    
    # 3. Botón de descarga utilizando el buffer
    st.download_button(
        label="Descargar Informe",
        data=buffer,
        file_name="Reporte_ESG.pdf",
        mime="application/pdf"
    )
