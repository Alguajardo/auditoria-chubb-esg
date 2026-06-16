import streamlit as st
from fpdf import FPDF
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis por Pilares", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS POR PILARES + GRÁFICA ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'], key="up1")
    texto = st.text_area("Pega el texto para análisis:", height=150, key="txt1")
    
    if st.button("Ejecutar Análisis", key="btn_ejecutar"):
        # Dashboard de métricas
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        st.markdown("---")
        
        # Gráfica e Interpretación
        col_grafico, col_explicacion = st.columns([1, 1])
        with col_grafico:
            st.subheader("Distribución de Riesgos")
            data = pd.DataFrame({"Valor": [20, 50, 30]}, index=["Gobernanza", "Estrategia", "Métricas"])
            st.bar_chart(data)
        
        with col_explicacion:
            st.subheader("Interpretación del Consultor")
            st.write("* **Estrategia:** Alta concentración de brechas; requiere vinculación financiera.")
            st.write("* **Métricas:** Debilidad crítica en Scope 3 (Párrafo 28).")
        
        st.markdown("---")
        st.subheader("Auditoría Detallada")
        tab_gob, tab_est, tab_riesgo, tab_met = st.tabs(["Gobernanza", "Estrategia", "Riesgos", "Métricas"])
        with tab_gob: st.info("Cumple con Párrafo 26.")
        with tab_est: st.warning("Falta horizonte temporal de 3 años (Párrafo 27).")
        with tab_riesgo: st.info("Identificados sin cuantificación financiera.")
        with tab_met: st.error("No se reporta alcance 3.")

# --- PESTAÑA 2: CHATBOT EXPERTO ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    norma_db = {
        "gobernanza": "Párrafo 26: El objetivo del requisito de gobernanza es permitir que los usuarios comprendan el gobierno corporativo.",
        "estrategia": "Párrafo 27: La entidad debe revelar cómo los riesgos afectan su modelo de negocio.",
        "alcance 3": "Párrafo 28: La entidad debe revelar emisiones de GEI de alcance 3."
    }
    consulta = st.text_input("Ingresa concepto (ej: gobernanza, estrategia):", key="chat2")
    if st.button("Consultar"):
        busqueda = consulta.strip().lower()
        encontrado = False
        for clave in norma_db:
            if clave in busqueda:
                st.success(f"Referencia para '{clave}':")
                st.info(norma_db[clave])
                encontrado = True
                break
        if not encontrado: st.warning("Concepto no encontrado.")

# --- PESTAÑA 3: GENERADOR DE INFORMES ---
with tab3:
    st.header("Generador de Informe Técnico - APA 7")
    empresa = st.text_input("Empresa Auditada")
    intro = st.text_area("Introducción:")
    brechas = st.text_area("Análisis:")
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 14)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True, align='C')
        pdf.set_font("Times", size=12)
        pdf.cell(0, 10, "Introducción", ln=True)
        pdf.multi_cell(0, 7, intro)
        pdf.cell(0, 10, "Análisis", ln=True)
        pdf.multi_cell(0, 7, brechas)
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
