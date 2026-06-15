import streamlit as st
from fpdf import FPDF
import os

st.title("Plataforma de Auditoría ESG")

if st.button("Generar Informe"):
    # 1. Definir ruta temporal
    temp_file = "Reporte_ESG.pdf"
    
    # 2. Crear el PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "INFORME DE AUDITORIA ESG", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, "Informe generado correctamente.", ln=True)
    
    # 3. Guardar directamente a archivo
    pdf.output(temp_file)
    
    # 4. Leer el archivo en binario y ofrecer descarga
    with open(temp_file, "rb") as f:
        pdf_bytes = f.read()
        
    st.download_button(
        label="Descargar Informe",
        data=pdf_bytes,
        file_name="Reporte_ESG.pdf",
        mime="application/pdf"
    )
    
    # Opcional: limpiar el archivo temporal tras la descarga
    # os.remove(temp_file)
