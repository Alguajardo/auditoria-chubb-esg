import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Auditoria ESG Pro", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicialización segura con valores numéricos estrictos
if 'resumen_dashboard' not in st.session_state:
    st.session_state.resumen_dashboard = {"Gobernanza": 20, "Estrategia": 50, "Riesgos": 30, "Metricas": 80}
if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {"Gobernanza": "Cumple.", "Estrategia": "Brecha detectada.", "Riesgos": "Cuantificar.", "Metricas": "Falta alcance 3."}

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
        
        # Dashboard en PDF
        pdf.set_font("Times", 'B', 12)
        pdf.cell(0, 10, "Resumen de Brechas (Dashboard)", ln=True)
        pdf.set_draw_color(0, 80, 180)
        pdf.rect(10, 30, 190, 40)
        
        pdf.set_y(35)
        pdf.set_font("Courier", size=10)
        # Forzamos conversión a entero con int() para evitar el TypeError
        for k, v in st.session_state.resumen_dashboard.items():
            valor_int = int(v)
            bar = "|" * (valor_int // 5)
            pdf.cell(0, 8, f"{k:<15} {bar} {valor_int}%", ln=True)
        
        # Detalle
        pdf.ln(20)
        for k, v in st.session_state.informe_data.items():
            pdf.set_font("Times", 'B', 12)
            pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 10, k, ln=True, fill=True)
            pdf.set_font("Times", size=11)
            pdf.multi_cell(0, 7, str(v))
            pdf.ln(2)
            
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
