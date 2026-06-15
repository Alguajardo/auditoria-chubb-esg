import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1 ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'], key="uploader_1")
    texto = st.text_area("O pega el texto aquí:", height=200, key="texto_analisis")
    if st.button("Ejecutar Análisis", key="btn_analisis"):
        st.success("Análisis técnico en curso...")

# --- PESTAÑA 2 ---
with tab2:
    st.header("Asistente Técnico ESG")
    consulta = st.text_input("Consulta IFRS S1/S2:", key="input_chatbot")
    if st.button("Consultar Normativa", key="btn_chatbot"):
        st.markdown("""
        **Pilares IFRS S1/S2:** 1. Gobernanza | 2. Estrategia | 3. Gestión de Riesgos | 4. Métricas.
        """)

# --- PESTAÑA 3: GENERADOR DE INFORMES TIPO ---
with tab3:
    st.header("Generador de Informe Técnico ESG")
    empresa = st.text_input("Empresa Auditada", key="empresa_nombre")
    
    # Estructura del Informe Tipo
    st.markdown("### Estructura de Informe:")
    brechas = st.text_area("Hallazgos (Filtrado Atómico - Párrafos):", 
                           "Ejemplo: Párrafo 15 - La memoria carece de métricas Scope 3.")
    
    impacto = st.number_input("Impacto Financiero Estimado (USD)", value=10000, key="impacto_val")
    probabilidad = st.slider("Probabilidad de Materialidad (%)", 0, 100, 50, key="prob_val")
    
    recomendaciones = st.text_area("Recomendaciones Estratégicas (IFRS S1/S2):", 
                                   "Ejemplo: Implementar comité de riesgos climáticos.")

    if st.button("Generar Informe PDF Estándar", key="btn_pdf_estandar"):
        pdf = FPDF()
        pdf.add_page()
        
        # Cabecera
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"INFORME TIPO: AUDITORIA ESG - {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        # Sección 1: Metodología
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "1. Metodologia: Filtrado Atomico", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 7, "Analisis realizado sobre la base de los parrafos seleccionados para verificar cumplimiento con IFRS S1 y S2.")
        
        # Sección 2: Brechas
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "2. Brechas Significativas Detectadas", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 7, brechas)
        
        # Sección 3: Conectividad Financiera
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "3. Analisis de Conectividad Financiera", ln=True)
        pdf.set_font("Arial", size=10)
        conectividad = impacto * (probabilidad / 100)
        pdf.cell(0, 7, f"Valor en Riesgo (Impacto * Probabilidad): ${conectividad:,.2f} USD", ln=True)
        
        # Sección 4: Recomendaciones
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, "4. Recomendaciones Estrategicas", ln=True)
        pdf.set_font("Arial", size=10)
        pdf.multi_cell(0, 7, recomendaciones)
        
        # Descarga
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe Técnico PDF", pdf_bytes, "Informe_ESG_Profesional.pdf", "application/pdf")
