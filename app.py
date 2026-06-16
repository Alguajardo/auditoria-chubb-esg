import streamlit as st
from fpdf import FPDF
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicialización de estado para persistencia de datos
if 'resumen_dashboard' not in st.session_state:
    st.session_state.resumen_dashboard = {"Gobernanza": 20, "Estrategia": 50, "Riesgos": 30, "Metricas": 80}
if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {
        "Introducción": "Análisis estratégico de convergencia con IFRS S1/S2.",
        "Gobernanza": "Cumple Párrafo 26; el comité de ética está activo.",
        "Estrategia": "Falta horizonte temporal de 3 años según Párrafo 27.",
        "Riesgos y Oportunidades": "Identificados riesgos climáticos; falta cuantificación.",
        "Métricas": "Crítico: No se reporta alcance 3 (Párrafo 28).",
        "Conclusiones": "Madurez operativa con brechas en reporte IFRS S2.",
        "Recomendaciones": "Vincular riesgos climáticos con el Estado de Resultados."
    }

tab1, tab2, tab3 = st.tabs(["📊 Análisis y Dashboard", "🤖 Chatbot ESG", "📄 Informe Tipo Australis"])

# Pestaña 1: Análisis y Dashboard
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'])
    if st.button("Ejecutar Análisis"):
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        st.subheader("Distribución de Riesgos")
        st.bar_chart(pd.DataFrame(st.session_state.resumen_dashboard, index=["Nivel de Brecha (%)"]).T)
        
        st.success("Análisis realizado: Datos listos para el informe.")

# Pestaña 2: Chatbot ESG
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    norma_db = {
        "gobernanza": "Párrafo 26: El objetivo es que los usuarios comprendan el gobierno corporativo para gestionar riesgos.",
        "estrategia": "Párrafo 27: La entidad debe revelar cómo los riesgos de sostenibilidad afectan su modelo de negocio.",
        "alcance 3": "Párrafo 28: La entidad debe revelar emisiones de GEI de alcance 3."
    }
    consulta = st.text_input("Ingresa concepto (ej: gobernanza, estrategia):")
    if st.button("Consultar"):
        b = consulta.strip().lower()
        found = False
        for k, v in norma_db.items():
            if k in b:
                st.success(f"Referencia técnica para '{k}':")
                st.info(v)
                found = True
        if not found: st.warning("Concepto no encontrado.")

# Pestaña 3: Informe Tipo Australis
with tab3:
    st.header("Generador de Informe ESG - Formato Corporativo")
    empresa = st.text_input("Nombre de la Empresa", "Australis Seafoods S.A.")
    
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        # Título
        pdf.set_font("Times", 'B', 18)
        pdf.cell(0, 15, f"INFORME ESG: {empresa}", ln=True, align='C')
        
        # Dashboard en PDF
        pdf.set_font("Times", 'B', 12)
        pdf.cell(0, 10, "Resumen de Brechas (Dashboard)", ln=True)
        pdf.set_draw_color(0, 80, 180)
        pdf.rect(10, 30, 190, 40)
        pdf.set_y(35)
        pdf.set_font("Courier", size=10)
        for k, v in st.session_state.resumen_dashboard.items():
            bar = "|" * (int(v) // 5)
            pdf.cell(0, 8, f"{k:<15} {bar} {v}%", ln=True)
        
        # Detalle por pilares
        pdf.ln(25)
        for titulo, contenido in st.session_state.informe_data.items():
            pdf.set_font("Times", 'B', 14)
            pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 10, titulo, ln=True, fill=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 8, str(contenido))
            pdf.ln(2)
            
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG_Final.pdf", "application/pdf")
