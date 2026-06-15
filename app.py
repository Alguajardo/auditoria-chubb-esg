# 2. Crear PDF
    pdf = FPDF()
    
    # IMPORTANTE: Aseguramos que siempre haya una página abierta al inicio
    pdf.add_page()

    def agregar_seccion(titulo, contenido, nueva_pagina=True):
        if nueva_pagina: 
            pdf.add_page()
        
        pdf.set_font("Arial", 'B', 16)
        pdf.cell(0, 10, titulo, ln=True)
        pdf.ln(5)
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, contenido)

    # --- LLAMADAS ---
    # La primera vez llamamos sin crear página nueva, 
    # pero como ya agregamos add_page() arriba, ya no dará error.
    agregar_seccion("Introducción", "Informe de auditoría técnica basado en estándares IFRS S1/S2.", False)
    
    # Las siguientes secciones sí pueden ir en páginas nuevas
    agregar_seccion("Perfil de la Empresa", perfil)
    # ... resto del código ...
