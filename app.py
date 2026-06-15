import streamlit as st
from fpdf import FPDF

st.title("Plataforma de Auditoría ESG")

if st.button("Generar Informe"):
    # Creamos el objeto PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INFORME DE AUDITORIA ESG", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, "Informe generado exitosamente.", ln=True)
    
    # Generamos los bytes del PDF usando fpdf2
    # El parámetro dest='S' devuelve el PDF como un string/bytes
    pdf_bytes = pdf.output(dest='S')
    
    st.download_button(
        label="Descargar Informe",
        data=pdf_bytes,
        file_name="Reporte_ESG.pdf",
        mime="application/pdf"
    )
