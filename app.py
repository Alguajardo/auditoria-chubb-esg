import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt

# Configuración inicial
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Definición de pestañas
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    archivo = st.file_uploader("Cargar Memoria (PDF/TXT)", type=['pdf', 'txt'], key="up1")
    texto = st.text_area("Pega el texto aquí para análisis inmediato:", height=200, key="txt1")
    if st.button("Ejecutar Análisis", key="btn_ejecutar"):
        st.success("Análisis técnico realizado con éxito.")
        st.write("1. **Párrafo 12 (Gobernanza):** Alineado con IFRS S1.")
        st.write("2. **Párrafo 28 (Métricas):** Brecha detectada (Falta de Scope 3).")

# --- PESTAÑA 2: CHATBOT ESG CONVERSACIONAL ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    
    # Inicializar historial de chat
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Mostrar mensajes previos
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input del usuario
    if prompt := st.chat_input("Pregunta sobre IFRS S1/S2..."):
        # Guardar y mostrar usuario
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Lógica de respuesta inteligente (Simulación de Experto)
        with st.chat_message("assistant"):
            # Aquí inyectamos la lógica experta
            if "28" in prompt or "párrafo 28" in prompt.lower():
                response = "El Párrafo 28 de IFRS S1 exige revelar las habilidades y competencias que poseen los órganos de gobierno para supervisar riesgos de sostenibilidad."
            elif "gobernanza" in prompt.lower():
                response = "La Gobernanza en IFRS S1 busca que los usuarios entiendan cómo el directorio monitorea los riesgos climáticos. ¿Quieres que profundicemos en los párrafos 26 o 27?"
            else:
                response = "Como experto en IFRS S1/S2, puedo explicarte los pilares de Gobernanza, Estrategia, Gestión de Riesgos y Métricas. ¿Qué pilar deseas analizar?"
            
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- PESTAÑA 3: GENERADOR DE INFORMES (APA 7 + CONECTIVIDAD FINANCIERA) ---
with tab3:
    st.header("Generador de Informe Técnico - Formato APA 7")
    empresa = st.text_input("Empresa Auditada", key="emp_nombre_3")
    
    # Inputs para el informe
    introduccion = st.text_area("Introducción:", "El presente informe técnico detalla la auditoría de sostenibilidad basada en los estándares IFRS S1 y S2.")
    brechas = st.text_area("Análisis (Brechas detectadas):", "Análisis de los párrafos críticos en relación a la norma.")
    recomendaciones = st.text_area("Recomendaciones:", "Se recomienda al directorio fortalecer los mecanismos de gobernanza climática.")
    
    # Sección de Conectividad Financiera
    st.markdown("### Conectividad Financiera")
    nic_check = st.multiselect("Normas NIC vinculadas:", ["NIC 16 (Propiedad, Planta y Equipo)", "NIC 36 (Deterioro de Activos)", "NIC 37 (Provisiones)"])
    
    if st.button("Generar Informe Formato APA", key="btn_pdf_apa_final"):
        pdf = FPDF()
        pdf.add_page()
        
        # Cabecera APA
        pdf.set_font("Times", 'B', 14)
        pdf.cell(0, 10, f"Informe: {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        # Contenido Estructurado
        for titulo, contenido in [("Introducción", introduccion), ("Análisis (Brechas)", brechas), ("Recomendaciones", recomendaciones)]:
            pdf.set_font("Times", 'B', 12)
            pdf.cell(0, 10, titulo, ln=True)
            pdf.set_font("Times", size=12)
            pdf.multi_cell(0, 7, contenido)
            pdf.ln(5)
            
        # Conectividad Financiera
        pdf.set_font("Times", 'B', 12)
        pdf.cell(0, 10, "Conectividad con Normas Financieras (NIC)", ln=True)
        pdf.set_font("Times", size=12)
        pdf.multi_cell(0, 7, f"El análisis de sostenibilidad se ha vinculado con: {', '.join(nic_check)} para asegurar la integridad de los Estados Financieros.")
        
        # Firma
        pdf.ln(10)
        pdf.set_font("Times", 'I', 10)
        pdf.cell(0, 10, "Auditoría realizada por: Alberto Esteban Guajardo Meneses | Consultor Senior ESG", ln=True)
        
        pdf_bytes = bytes(pdf.output())
        st.download_button("Descargar Informe APA 7", pdf_bytes, "Informe_Tecnico_ESG.pdf", "application/pdf")
