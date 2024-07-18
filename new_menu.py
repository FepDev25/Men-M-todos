import tkinter as tk
from tkinter import ttk
from tkinter_custom_button import TkinterCustomButton
from biseccion import *
from falsa_pocision import *
from newton_raphson import *
from regresion import *
from secante import *

def biseccion(frame):
    biseccion_method_window(frame)

def falsa_posicion(frame):
    falsa_pocision_method_window(frame)

def newton_raphson(frame):
    newton_raphsonn_method_window(frame)

def secante(frame):
    secante_method_window(frame)

def regresion(frame):
    regresion_window(frame)

def limpiar_frame():
    for widget in framePrincipal.winfo_children():
        widget.destroy()

def create_custom_button(text, command, frame):
    custom_button = TkinterCustomButton(
        master=frame,
        bg_color="#2C3E50",
        fg_color="#212F3D",
        border_color="#117A65",
        hover_color="#34495E",
        text_font=None,
        text=text,
        text_color="white",
        corner_radius=12,
        border_width=4,
        width=180 if len(text) > 10 else 100,
        height=60,
        hover=True,
        command=command)
    return custom_button

def mostrar_ecuaciones_lineales():
    limpiar_frame()
    label = ttk.Label(framePrincipal, text="Contenido de Ecuaciones Lineales")
    label.pack(padx=10, pady=10)

def mostrar_ecuaciones_no_lineales():
    limpiar_frame()
    
    # Frame para Métodos Cerrados
    frameCerrados = ttk.Frame(framePrincipal)
    frameCerrados.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    labelCerrados = ttk.Label(frameCerrados, text="Métodos Cerrados")
    labelCerrados.pack(pady=5)
    
    botonBiseccion = create_custom_button("Bisección", lambda: biseccion(frameCerrados), frameCerrados)
    botonBiseccion.pack(pady=5)
    
    botonFalsePosicion = create_custom_button("Falsa Posición", lambda: falsa_pocision(frameCerrados), frameCerrados)
    botonFalsePosicion.pack(pady=5)
    
    # Frame para Métodos Abiertos
    frameAbiertos = ttk.Frame(framePrincipal)
    frameAbiertos.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    labelAbiertos = ttk.Label(frameAbiertos, text="Métodos Abiertos")
    labelAbiertos.pack(pady=5)
    
    botonNewtonRaphson = create_custom_button("Newton-Raphson", lambda: newton_raphson(frameAbiertos), frameAbiertos)
    botonNewtonRaphson.pack(pady=5)
    
    botonSecante = create_custom_button("Secante", lambda: secante(frameAbiertos), frameAbiertos)
    botonSecante.pack(pady=5)

    # Frame indicaciones

    frameIndicaciones = ttk.Frame(framePrincipal)
    frameIndicaciones.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=30, pady=30)

    indicaciones = """Indicaciones:
    Las funciones se deben ingresar en términos de x. Ej: x + 45
    Se debe incluir los signos en cada una de las operaciones. Ej: 2*x + 3*x - (3*x/5) - 12
    Para potencias se debe utilizar "**". Ej: x**2 - 13
    Pra funciones trigonométricas usar: sin(x), cos(x), tan(x)
    Para constantes utilizar: "pi" para el numero Pi. "E" para el numero de euler.
    Para logaritmos utilizar: "ln(x)" para logaritmo natural. "log(x, grado)" para logaritmos de diferente base. Ej: log(x, 10) + 9
    Para indicar decimales su usa el punto. Ej: 3.7*x - 15
    """
    labelIndicaciones = ttk.Label(frameIndicaciones, text=indicaciones)
    labelIndicaciones.pack(pady=5)

def mostrar_regresion():
    limpiar_frame()

    # Frame para Regresion

    frameRegresion = ttk.Frame(framePrincipal)
    frameRegresion.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)

    labelRegresion = ttk.Label(frameRegresion, text="Regresión")
    labelRegresion.pack(pady=5)

    botonRegresion = create_custom_button("Regresión", lambda: regresion(frameRegresion), frameRegresion)
    botonRegresion.pack(pady=5)

def mostrar_interpolacion():
    limpiar_frame()
    label = ttk.Label(framePrincipal, text="Contenido de Interpolación")
    label.pack(padx=10, pady=10)

def mostrar_diferenciacion_numerica():
    limpiar_frame()
    label = ttk.Label(framePrincipal, text="Contenido de Diferenciación Numérica")
    label.pack(padx=10, pady=10)

def mostrar_integracion_numerica():
    limpiar_frame()
    label = ttk.Label(framePrincipal, text="Contenido de Integración Numérica")
    label.pack(padx=10, pady=10)

def mostrar_ecuaciones_diferenciales():
    limpiar_frame()
    
    # Frame para Métodos Cerrados
    frameEueler = ttk.Frame(framePrincipal)
    frameEueler.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    labelEuler = ttk.Label(frameEueler, text="Métodos de Euler")
    labelEuler.pack(pady=5)
    
    botonBiseccion = create_custom_button("Euler", lambda: print(""), frameEueler)
    botonBiseccion.pack(pady=5)
    
    botonFalsePosicion = create_custom_button("Euler Mejorado", lambda: print(""), frameEueler)
    botonFalsePosicion.pack(pady=5)
    
    # Frame para Métodos Abiertos
    frameRK = ttk.Frame(framePrincipal)
    frameRK.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, padx=10, pady=10)
    
    labelFk = ttk.Label(frameRK, text="Runge Kuta")
    labelFk.pack(pady=5)
    
    botonNewtonRaphson = create_custom_button("Runge Kuta 4to Orden", lambda: print(""), frameRK)
    botonNewtonRaphson.pack(pady=5)

root = tk.Tk()
root.title("Métodos Numéricos")
root.geometry("1350x400")  

ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

ancho_ventana = 1350
alto_ventana = 400
x = (ancho_pantalla // 2) - (ancho_ventana // 2)
y = (alto_pantalla // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

frameBotones = ttk.Frame(root)
frameBotones.pack(side=tk.TOP, fill=tk.X)

framePrincipal = ttk.Frame(root)
framePrincipal.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

botones = [
    ("Ecuaciones Lineales", mostrar_ecuaciones_lineales),
    ("Ecuaciones no Lineales", mostrar_ecuaciones_no_lineales),
    ("Regresión", mostrar_regresion),
    ("Interpolación", mostrar_interpolacion),
    ("Diferenciación Numérica", mostrar_diferenciacion_numerica),
    ("Integración Numérica", mostrar_integracion_numerica),
    ("Ecuaciones Diferenciales", mostrar_ecuaciones_diferenciales)
]

for texto_boton, metodo in botones:
    boton = create_custom_button(texto_boton, metodo, frameBotones)
    boton.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
