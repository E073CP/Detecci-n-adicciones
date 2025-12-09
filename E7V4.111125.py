# importamos las bibliotecas
import tkinter as tk
from tkinter import ttk

# configuración de colores y fuentes
COLOR_FONDO = "#FFDDF8"
COLOR_MENU = "#8C8C91"
COLOR_TEXTO = "#CF3333"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# ventana principal
root = tk.Tk()
root.title("Software de detección de adicciones a las redes sociales")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# configuramos el frame del menú lateral
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="right", fill="y")

# contenido del frame principal
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="left", fill="both", expand=True)

# función para cambiar de página
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# página de bienvenida
def pagina_bienvenida():
    tk.Label(
        contenido_frame, 
        text="Bienvenido al software de detección de adicciones a las redes sociales", 
        font=FUENTE_TITULO, bg=COLOR_FONDO, wraplength=600
    ).pack(pady=30)
    tk.Label(
        contenido_frame, 
        text="Selecciona una opción en el menú para continuar.", 
        font=FUENTE_TEXTO, bg=COLOR_FONDO, wraplength=600
    ).pack(pady=10)
    tk.Label(
        contenido_frame, 
        text="Este software te ayudará a detectar si padeces adicción a la tecnología.", 
        font=FUENTE_TEXTO, bg=COLOR_FONDO, wraplength=600
    ).pack(pady=10)
    tk.Label(
        contenido_frame, 
        text="TU SALUD ES IMPORTANTE", 
        font=FUENTE_TITULO, bg=COLOR_FONDO
    ).pack(pady=10)

# página de inicio de sesión / registro
def pagina_registro():
    tk.Label(contenido_frame, text="Inicio de sesión de usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    for campo in ["Nombre", "Correo"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)
    ttk.Button(contenido_frame, text="Iniciar sesión").pack(pady=10)

# página del test
def pagina_test():
    tk.Label(contenido_frame, text="Test de bienestar digital", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(
        contenido_frame, 
        text="Responde las siguientes preguntas para conocer tu nivel de bienestar en relación con las redes sociales.",
        wraplength=600, bg=COLOR_FONDO, font=FUENTE_TEXTO
    ).pack(pady=10)
    ttk.Button(contenido_frame, text="Ver resultados", command=lambda: mostrar_pagina("Resultados")).pack(pady=20)

# página de resultados
def pagina_resultados():
    tk.Label(contenido_frame, text="Resultados del test de adicción a redes sociales", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(
        contenido_frame, 
        text="Aquí se mostrarán los resultados del test una vez completado.", 
        bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600
    ).pack(pady=10)
    ttk.Button(contenido_frame, text="Volver al inicio", command=lambda: mostrar_pagina("Bienvenida")).pack(pady=20)

# página de síntomas y señales
def pagina_sintomasyseñales():
    tk.Label(contenido_frame, text="Síntomas y señales", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    texto = (
        "Algunos síntomas comunes de la adicción a las redes sociales incluyen:\n\n"
        "• Pensar constantemente en las redes sociales, incluso cuando no las estás usando.\n"
        "• Dificultad para reducir el tiempo de uso, a pesar de intentos previos.\n"
        "• Uso excesivo como escape emocional, evitando problemas personales o el estrés diario.\n"
        "• Síntomas de abstinencia, como ansiedad o irritabilidad al no poder acceder a las plataformas.\n"
        "• Impacto en la vida diaria, como descuidar el trabajo, estudios o relaciones interpersonales."
    )
    tk.Label(contenido_frame, text=texto, bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600, justify="left").pack(pady=10)
    ttk.Button(contenido_frame, text="Volver al inicio", command=lambda: mostrar_pagina("Bienvenida")).pack(pady=20)

# página de historias inspiradoras 
def pagina_historiasinspiradoras():
    tk.Label(contenido_frame, text="Historias inspiradoras", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(contenido_frame, text="Aquí se mostrarán las historias de los usuarios.", bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600).pack(pady=10)
    ttk.Button(contenido_frame, text="Volver al inicio", command=lambda: mostrar_pagina("Bienvenida")).pack(pady=20)

# página de ayuda al usuario
def pagina_ayudaalusuario():
    tk.Label(contenido_frame, text="Ayuda al usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(
        contenido_frame, 
        text="Aquí podrás enviar tus quejas o solicitar asistencia en caso de algún problema con el software.",
        bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600, justify="left"
    ).pack(pady=10)
    ttk.Button(contenido_frame, text="Volver al inicio", command=lambda: mostrar_pagina("Bienvenida")).pack(pady=20)

    # página de cerrar secion
def pagina_serrarsesion ():
    tk.Label(contenido_frame, text="cerrar sesion", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(
        contenido_frame, 
        text="Aquí podrás cerrar tu sesion.",
        bg=COLOR_FONDO, font=FUENTE_TEXTO, wraplength=600, justify="left"
    ).pack(pady=10)
    ttk.Button(contenido_frame, text="cerrar sesion", command=lambda: mostrar_pagina("Registro")).pack(pady=20)


# diccionario de páginas
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,     
    "Resultados": pagina_resultados,
    "Síntomas y señales": pagina_sintomasyseñales,
    "Historias inpiradoras": pagina_historiasinspiradoras,
    "Ayuda al usuario": pagina_ayudaalusuario,
    "cerrar sesion":pagina_serrarsesion,
}

# botones del menú lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

# botón salir
ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# mostrar página inicial
pagina_bienvenida()

# ejecutar la aplicación
root.mainloop()