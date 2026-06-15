import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")

# --- MENÚ DE NAVEGACIÓN ---
menu = st.sidebar.selectbox("Selecciona Módulo", ["Análisis de Documentos", "Chatbot ESG", "Generador de Informes"])

# --- MÓDULO 1: ANÁLISIS DE BRECHAS ---
if menu == "Análisis de Documentos":
    st.header("Carga de Memorias y Estados Financieros")
    archivo = st.file_uploader("Sube Memorias o EEFF", type=['pdf', 'xlsx', 'txt'])
    if archivo:
        st.write("Analizando brechas y materialidad...")
        # Aquí iría tu lógica de filtrado atómico
        st.success("Análisis completado: Brechas detectadas.")

# --- MÓDULO 2: CHATBOT ESG ---
elif menu == "Chatbot ESG":
    st.header("Asistente Técnico ESG")
    pregunta = st.text_input("Consulta sobre IFRS S1/S2 o NCG 461")
    if st.button("Consultar"):
        st.write("Respuesta técnica basada en tu base de conocimiento...")

# --- MÓDULO 3: GENERADOR DE INFORMES ---
elif menu == "Generador de Informes":
    st.header("Generación de Informe Ejecutivo")
    empresa = st.text_input("Empresa")
    # ... (aquí va el formulario que ya teníamos para generar el PDF)
    if st.button("Generar PDF"):
        st.write("Generando documento final...")
