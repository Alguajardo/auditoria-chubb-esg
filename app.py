import streamlit as st
from fpdf import FPDF
import pandas as pd

st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Estado persistente para auditoría
if 'auditoria_data' not in st.session_state:
    st.session_state.auditoria_data = {
        "Gobernanza": "Cumple Párrafo 26; comité de ética activo y Modelo de Prevención del Delito actualizado.",
        "Estrategia": "Brecha: Falta horizonte temporal de 3 años según Párrafo 27. Requiere integración vertical.",
        "Riesgos y Oportunidades": "Identificados riesgos climáticos y operativos; falta cuantificación financiera.",
        "Métricas y Objetivos": "Crítico: No se reporta alcance 3 (Párrafo 28). Desperdicio bajo control.",
        "Conectividad": "Débil vínculo entre los riesgos de sostenibilidad identificados y el Estado de Resultados."
    }

tab1, tab2, tab3 = st.tabs(["📊 Análisis y Dashboard", "🤖 Chatbot ESG", "📄 Informe Corporativo"])

# PESTAÑA 1: DASHBOARD Y ANÁLISIS DETALLADO
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'])
    if st.button("Ejecutar Análisis"):
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Gobernanza", "OK")
        c2.metric("Estrategia", "Brecha", "-1")
        c3.metric("Riesgos", "OK")
        c4.metric("Métricas", "Crítico", "!")
        
        st.markdown("---")
        col_g, col_e = st.columns([1, 1])
        with col_g:
            st.subheader("Distribución de Riesgos")
            st.bar_chart(pd.DataFrame({"Brecha (%)": [20, 50, 30, 80, 70]}, index=["Gob", "Est", "Riesgos", "Met", "Conect"]))
        with col_e:
            st.subheader("Comentarios de Brechas")
            for k, v in st.session_state.auditoria_data.items():
                st.write(f"**{k}:** {v}")
            
        st.subheader("Auditoría Detallada por Pilares")
        t1, t2, t3, t4, t5 = st.tabs(["Gobernanza", "Estrategia", "Riesgos", "Métricas", "Conectividad"])
        with t1: st.info(st.session_state.auditoria_data["Gobernanza"])
        with t2: st.warning(st.session_state.auditoria_data["Estrategia"])
        with t3: st.info(st.session_state.auditoria_data["Riesgos y Oportunidades"])
        with t4: st.error(st.session_state.auditoria_data["Métricas y Objetivos"])
        with t5: st.warning(st.session_state.auditoria_data["Conectividad"])

# PESTAÑA 2: CHATBOT
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    norma_db = {"gobernanza": "Párrafo 26: Gobierno corporativo.", "estrategia": "Párrafo 27: Modelo de negocio.", "alcance 3": "Párrafo 28: Emisiones GEI."}
    consulta = st.text_input("Ingresa concepto técnico:")
    if st.button("Consultar"):
        for k, v in norma_db.items():
            if k in consulta.lower(): st.info(v)

# PESTAÑA 3: INFORME CORPORATIVO
with tab3:
    st.header("Generador de Informe ESG")
    empresa = st.text_input("Empresa Auditada", "Ingrese nombre...")
    
    st.subheader("Validación de Contenidos")
    for k, v in st.session_state.auditoria_data.items():
        st.info(f"**{k}:** {v}")
    
    if st.button("Generar Informe PDF"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Times", 'B', 18)
        pdf.cell(0, 15, f"INFORME ESG: {empresa}", ln=True, align='C')
        
        pdf.set_draw_color(0, 80, 180)
        pdf.rect(10, 30, 190, 30)
        pdf.set_y(35)
        pdf.set_font("Courier", size=10)
        pdf.cell(0, 8, "Dashboard de Brechas (Resumen Ejecutivo)", ln=True)
        pdf.cell(0, 8, "Nivel de Brechas: [|||||.......] 50% promedio", ln=True)
        
        pdf.ln(20)
        for titulo, contenido in st.session_state.auditoria_data.items():
            pdf.set_font("Times", 'B', 14)
            pdf.set_fill_color(240, 240, 240)
            pdf.cell(0, 10, titulo, ln=True, fill=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 8, str(contenido))
            pdf.ln(2)
            
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe PDF", pdf_bytes, "Informe_ESG.pdf", "application/pdf")
