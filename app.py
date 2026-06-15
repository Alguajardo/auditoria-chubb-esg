import streamlit as st
from fpdf import FPDF

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
    
    # 2. Generar el contenido en memoria
    # Usamos .output(dest='S') para obtener el contenido como string/bytes
    pdf_output = pdf.output(dest='S')
    
    # 3. Convertir explícitamente a bytes (esto soluciona el error)
    if isinstance(pdf_output, str):
        pdf_bytes = pdf_output.encode('latin-1')
    else:
        pdf_bytes = pdf_output
    
    # 4. Botón de descarga con bytes puros
    st.download_button(
        label="Descargar Informe",
        data=pdf_bytes,
        file_name="Reporte_ESG.pdf",
        mime="application/pdf"
    )
