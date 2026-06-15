import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

st.set_page_config(page_title="Auditoría ESG Pro", layout="wide")
st.title("Plataforma de Auditoría ESG - Informe Ejecutivo")

# --- Formulario de Entrada ---
with st.sidebar:
    st.header("Entrada de Datos")
    empresa = st.text_input("Nombre de la Empresa")
    perfil = st.text_area("Perfil de la Empresa")
    materialidad = st.text_area("Análisis de Materialidad")
    st.subheader("Filtrado Atómico")
    s1 = st.slider("Avance IFRS S1 (%)", 0, 100, 50)
    s2 = st.slider("Avance IFRS S2 (%)", 0, 100, 50)
    conectividad = st.text_area("Conectividad Financiera")
    hallazgos = st.text_area("Base de Datos de Hallazgos")
    recomendaciones = st.text_area("Recomendaciones")
    conclusiones = st.text_area("Conclusiones")

# --- Función definida fuera del botón para evitar errores ---
def agregar_seccion(pdf, titulo, contenido, nueva_pagina=True):
    if nueva_pagina:
        pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, titulo, ln=True)
    pdf.ln(5)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, contenido)

if st.button("Generar Informe Completo"):
    # 1. Generar Gráfica
    fig, ax = plt.subplots()
    ax.bar(['IFRS S1', 'IFRS S2'], [s1, s2], color=['#4F81BD', '#C0504D'])
    ax.set_ylim(0, 100)
    ax.set_title("Nivel de Cumplimiento IFRS")
    plt.savefig("grafica.png")
    
    # 2. Crear PDF
    pdf = FPDF()
    pdf.add_page()
    
    # 3. Construir secciones
    agregar_seccion(pdf, "Introducción", "Informe de auditoría técnica basado en estándares IFRS S1/S2.", False)
    agregar_seccion(pdf, "Perfil de la Empresa", perfil)
    agregar_seccion(pdf, "Materialidad", materialidad)
    agregar_seccion(pdf, "Filtrado Atómico (Brechas IFRS S1/S2)", f"Avance S1: {s1}%\nAvance S2: {s2}%")
    
    pdf.image("grafica.png", x=10, y=None, w=100)
    
    agregar_seccion(pdf, "Conectividad Financiera", conectividad)
    agregar_seccion(pdf, "Base de Datos de Hallazgos", hallazgos)
    agregar_seccion(pdf, "Recomendaciones", recomendaciones)
    agregar_seccion(pdf, "Conclusiones", conclusiones)

    # 4. Preparar descarga
    pdf_bytes = pdf.output(dest='S').encode('latin-1')
    st.download_button("Descargar Informe Completo", pdf_bytes, f"Informe_{empresa}.pdf", "application/pdf")
