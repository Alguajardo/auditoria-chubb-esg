import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Auditoría ESG Pro", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicialización segura
if 'resumen_dashboard' not in st.session_state:
    st.session_state.resumen_dashboard = {"Gobernanza": 20, "Estrategia": 50, "Riesgos": 30, "Métricas": 80}
if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {"Gobernanza": "Cumple Párrafo 26.", "Estrategia": "Brecha en horizonte temporal.", "Riesgos": "Falta cuantificación.", "Métricas": "Crítico: No reporta alcance 3."}

tab1, tab2, tab3 = st.tabs(["📊 Análisis y Dashboard", "🤖 Chatbot ESG", "📄 Informe Tipo Australis"])

with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    if st.button("Ejecutar Análisis"):
        st.bar_chart(pd.DataFrame(st.session_state.resumen_dashboard, index=["Nivel de Brecha (%)"]).T)
        st.success("Análisis ejecutado.")

with tab3:
    st.header("Generador de Informe ESG")
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 16)
        pdf.cell(0, 10, "INFORME EJECUTIVO ESG", ln=True, align='C')
        
        # 1. RECUADRO DE DASHBOARD
        pdf.set_font("Times", 'B', 12)
        pdf.cell(0, 10, "Dashboard de Brechas (Resumen)", ln=True)
        pdf.set_draw_color(0, 80, 180) # Azul corporativo
        pdf.rect(10, 30, 190, 40) # Recuadro
        
        # 2. GRÁFICO SIMULADO DENTRO DEL PDF
        pdf.set_y(35)
        pdf.set_font("Courier", size=10)
        for k, v in st.session_state.resumen_dashboard.items():
            bar = "|" * (v // 5) # Representación visual
            pdf.cell(0, 8, f"{k:<15} {bar} {v}%", ln=True)
        
        # 3. DETALLE POR PILARES
        pdf.ln(20)
        pdf.set_font("Times", 'B', 12)
        for k, v in st.session_state.informe_data.items():
            pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 10, k, ln=True, fill=True)
            pdf.set_font("Times", size=11)
            pdf.multi_cell(0, 7, v)
            pdf.ln(2)
            
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG_Final.pdf", "application/pdf")
