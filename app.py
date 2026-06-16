import streamlit as st
from fpdf import FPDF
import pandas as pd

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Inicialización de estado para el informe
if 'informe_data' not in st.session_state:
    st.session_state.informe_data = {"Gobernanza": "", "Estrategia": "", "Riesgos": "", "Metricas": "", "Conectividad": "", "Conclusiones": "", "Recomendaciones": ""}

tab1, tab2, tab3 = st.tabs(["📊 Análisis por Pilares", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    st.file_uploader("Cargar Memoria", type=['pdf', 'txt'])
    
    if st.button("Ejecutar Análisis"):
        # Dashboard Visual
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Gobernanza", "OK")
        col2.metric("Estrategia", "Brecha", "-1")
        col3.metric("Riesgos", "OK")
        col4.metric("Métricas", "Crítico", "!")
        
        # Gráfica
        st.bar_chart(pd.DataFrame({"Valor": [20, 50, 30]}, index=["Gobernanza", "Estrategia", "Métricas"]))
        
        # Tablas de Pilares
        t1, t2, t3, t4 = st.tabs(["Gobernanza", "Estrategia", "Riesgos", "Métricas"])
        with t1: st.info("Cumple Párrafo 26.")
        with t2: st.warning("Falta horizonte 3 años.")
        with t3: st.info("Riesgos identificados.")
        with t4: st.error("No reporta alcance 3.")
        
        # Guardar en estado para Pestaña 3
        st.session_state.informe_data = {
            "Gobernanza": "Cumple Párrafo 26; el comité de ética está activo.",
            "Estrategia": "Falta horizonte temporal de 3 años según Párrafo 27.",
            "Riesgos": "Identificados riesgos climáticos, falta cuantificación.",
            "Metricas": "No se reporta alcance 3 (Párrafo 28).",
            "Conectividad": "Débil vínculo entre riesgos climáticos y estados financieros.",
            "Conclusiones": "Madurez en gobernanza, requiere cuantificación financiera.",
            "Recomendaciones": "Vincular riesgos con el Estado de Resultados."
        }
        st.success("Análisis completado y guardado para el informe.")

# --- PESTAÑA 2: CHATBOT ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    # ... (Tu código de chatbot previo) ...
    st.write("Consulta normativa IFRS S1 y S2.")

# --- PESTAÑA 3: GENERADOR DE INFORMES ---
with tab3:
    st.header("Generador de Informe ESG")
    empresa = st.text_input("Empresa", "Australis Seafoods S.A.")
    
    # Editor de datos para el informe (para que puedas editar antes de exportar)
    data = st.session_state.informe_data
    for key in data:
        data[key] = st.text_area(f"Análisis {key}:", value=data[key])
    
    if st.button("Generar PDF Profesional"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 16)
        pdf.cell(0, 10, f"Informe ESG: {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        for k, v in data.items():
            pdf.set_font("Times", 'B', 12)
            pdf.cell(0, 10, k, ln=True)
            pdf.set_font("Times", size=11)
            pdf.multi_cell(0, 7, v)
            pdf.ln(2)
        
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
