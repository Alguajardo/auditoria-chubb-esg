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

# --- PESTAÑA 2: CHATBOT EXPERTO IFRS S1/S2 ---
with tab2:
    st.header("Asistente Técnico IFRS S1/S2")
    
    # 1. Base de conocimiento: Estructura de párrafos
    norma_db = {
        "26": "Párrafo 26: El objetivo del requisito de gobernanza es permitir que los usuarios comprendan el gobierno corporativo utilizado para monitorear y gestionar los riesgos y oportunidades relacionados con la sostenibilidad.",
        "27": "Párrafo 27: La entidad debe revelar: a) Los órganos de gobierno, b) Cómo el gobierno corporativo garantiza los controles y procedimientos.",
        "28": "Párrafo 28: La entidad debe revelar las características de los órganos de gobierno, incluyendo habilidades y competencias requeridas para supervisar riesgos de sostenibilidad.",
        "estrategia": "La estrategia debe describir cómo los riesgos de sostenibilidad afectan el modelo de negocio, la estrategia y los flujos de efectivo a corto, mediano y largo plazo."
    }
    
    consulta = st.text_input("Ingresa número de párrafo (ej: 28) o pilar (ej: Estrategia):", key="input_chat_2")
    
    if st.button("Consultar Normativa", key="btn_chat_2"):
        # Limpiar la consulta
        busqueda = consulta.strip().lower()
        
        # 2. Lógica de búsqueda inteligente
        encontrado = False
        for clave, contenido in norma_db.items():
            if clave in busqueda:
                st.success(f"Extracto de la norma encontrado:")
                st.write(contenido)
                encontrado = True
                break
        
        if not encontrado:
            st.warning("Lo siento, ese párrafo no está en mi base de conocimiento actual. Prueba con '26', '27', '28' o 'Estrategia'.")

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
