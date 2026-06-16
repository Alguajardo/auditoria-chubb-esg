import streamlit as st
from fpdf import FPDF
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis por Pilares", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: DASHBOARD ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria", type=['pdf', 'txt'])
    texto = st.text_area("Pega el texto para análisis:", height=150)
    
    if st.button("Ejecutar Análisis"):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        st.markdown("---")
        
        col_g, col_e = st.columns([1, 1])
        with col_g:
            st.subheader("Distribución de Riesgos")
            st.bar_chart(pd.DataFrame({"Valor": [20, 50, 30]}, index=["Gobernanza", "Estrategia", "Métricas"]))
        with col_e:
            st.subheader("Interpretación")
            st.write("- **Estrategia:** Alta brecha, requiere enfoque financiero.")
            st.write("- **Métricas:** Crítico en Scope 3.")
            
        tab_g, tab_e, tab_r, tab_m = st.tabs(["Gobernanza", "Estrategia", "Riesgos", "Métricas"])
        with tab_g: st.info("Cumple Párrafo 26.")
        with tab_e: st.warning("Falta horizonte 3 años (Párrafo 27).")
        with tab_r: st.info("Falta cuantificación financiera.")
        with tab_m: st.error("No se reporta alcance 3.")

# --- PESTAÑA 2: CHATBOT ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    norma_db = {
        "gobernanza": "Párrafo 26: El objetivo del requisito de gobernanza es permitir que los usuarios comprendan el gobierno corporativo.",
        "estrategia": "Párrafo 27: La entidad debe revelar cómo los riesgos afectan su modelo de negocio.",
        "alcance 3": "Párrafo 28: La entidad debe revelar emisiones de GEI de alcance 3."
    }
    consulta = st.text_input("Ingresa concepto (ej: gobernanza, estrategia):")
    if st.button("Consultar"):
        b = consulta.strip().lower()
        found = False
        for k in norma_db:
            if k in b:
                st.success(f"Referencia para '{k}':")
                st.info(norma_db[k])
                found = True
        if not found: st.warning("Concepto no encontrado.")

# --- PESTAÑA 3: INFORME TIPO AUSTRALIS ---
with tab3:
    st.header("Generador de Informe Técnico - Formato ESG")
    empresa = st.text_input("Empresa", "Australis Seafoods S.A.")
    intro = st.text_area("Introducción:", "Este análisis ESG aplica convergencia estratégica de estándares IFRS S1/S2.")
    analisis = st.text_area("Análisis:", "La empresa estructura su gobernanza bajo principios de integridad.")
    
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 16)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True, align='C')
        pdf.set_font("Times", size=12)
        pdf.cell(0, 10, "Introducción", ln=True)
        pdf.multi_cell(0, 7, intro)
        pdf.cell(0, 10, "Análisis", ln=True)
        pdf.multi_cell(0, 7, analisis)
        
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
