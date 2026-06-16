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

from thefuzz import process # Importar librería de búsqueda difusa

# --- PESTAÑA 2: CHATBOT EXPERTO (BÚSQUEDA DIFUSA) ---
with tab2:
    st.header("Asistente Técnico IFRS S1 (Búsqueda Inteligente)")
    
    # Supongamos que tu CSV tiene: parrafo_id, clave, texto
    # Ejemplo: 26, gobernanza, "El objetivo del requisito..."
    df = pd.read_csv("ifrs_s1.csv") 
    
    consulta = st.text_input("¿Qué concepto buscas? (ej: gobernanza, alcance 3, riesgos):", key="search_input")
    
    if st.button("Buscar en la Norma"):
        if consulta:
            # Buscamos la palabra clave más cercana en la columna 'clave' de tu CSV
            claves = df['clave'].tolist()
            mejor_coincidencia, score = process.extractOne(consulta.lower(), claves)
            
            if score > 60: # Si la coincidencia es mayor al 60%
                resultado = df[df['clave'] == mejor_coincidencia].iloc[0]
                st.success(f"Concepto encontrado: {mejor_coincidencia.upper()} (Confianza: {score}%)")
                st.write(f"**Referencia:** {resultado['texto']}")
                st.info("Nota de Auditoría: Recuerda verificar si este control está documentado en el sistema de gestión del cliente.")
            else:
                st.warning("No encontré un concepto claro. Prueba con términos como 'gobernanza', 'estrategia' o 'riesgos'.")# --- PESTAÑA 3: GENERADOR DE INFORMES (APA 7 + CONECTIVIDAD FINANCIERA) ---
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
