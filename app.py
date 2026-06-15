import streamlit as st
from fpdf import FPDF
import matplotlib.pyplot as plt
import io

# Configuración inicial de la página
st.set_page_config(page_title="Plataforma Auditoría ESG", layout="wide")
st.title("Plataforma Integral de Auditoría ESG")

# Pestañas de navegación
tab1, tab2, tab3 = st.tabs(["📊 Análisis y Filtrado Atómico", "🤖 Chatbot ESG", "📄 Generador de Informes"])

# --- PESTAÑA 1: ANÁLISIS Y FILTRADO ---
with tab1:
    st.header("Análisis de Brechas (Filtrado Atómico)")
    # Permite subir varios archivos, incluyendo PDFs y Excel
    archivos = st.file_uploader("Cargar Memorias y Estados Financieros", 
                                type=['pdf', 'txt', 'csv', 'xlsx'], 
                                accept_multiple_files=True)
    
    if archivos:
        st.success(f"Se han cargado {len(archivos)} archivos.")
        for archivo in archivos:
            st.write(f"✅ Procesando: {archivo.name}")
            # Aquí se procesaría el contenido de cada archivo cargado

# --- PESTAÑA 2: CHATBOT ESG ---
with tab2:
    st.header("Asistente Técnico ESG")
    consulta = st.text_input("Realiza tu consulta técnica sobre IFRS S1/S2:")
    if st.button("Enviar Consulta"):
        st.info("Procesando consulta en base de datos técnica...")
        # Aquí puedes integrar tu lógica de RAG o llamada a API

# --- PESTAÑA 3: GENERADOR DE INFORMES ---
with tab3:
    st.header("Generador de Informe Ejecutivo")
    
    # Formulario de datos
    empresa = st.text_input("Nombre de la Empresa")
    col1, col2 = st.columns(2)
    with col1:
        s1 = st.slider("Avance IFRS S1 (%)", 0, 100, 50)
    with col2:
        s2 = st.slider("Avance IFRS S2 (%)", 0, 100, 50)
    
    observaciones = st.text_area("Observaciones y Recomendaciones")

    if st.button("Generar Informe PDF"):
        # 1. Generar Gráfica de cumplimiento
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(['IFRS S1', 'IFRS S2'], [s1, s2], color=['#2E86C1', '#C0392B'])
        ax.set_ylim(0, 100)
        ax.set_title("Nivel de Cumplimiento")
        
        # Guardar gráfica en buffer
        img_buffer = io.BytesIO()
        plt.savefig(img_buffer, format='png')
        img_buffer.seek(0)
        
        # 2. Construir el PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, f"Informe de Auditoría: {empresa}", ln=True, align='C')
        pdf.ln(10)
        
        # Insertar Gráfica
        pdf.image(img_buffer, x=50, w=100)
        pdf.ln(90)
        
        # Cuerpo
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, f"Avance IFRS S1: {s1}%\nAvance IFRS S2: {s2}%\n\nObservaciones:\n{observaciones}")
        
        # 3. Descarga
        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        st.download_button("Descargar Informe Completo", pdf_bytes, "Informe_Auditoria.pdf", "application/pdf")
