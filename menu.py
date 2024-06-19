import tkinter as tk
from biseccion import *
from falsa_pocision import *
from newton_raphson import *
from secante import *
from tkinter_custom_button import TkinterCustomButton

color_fondo = "#2C3E50"

def create_custom_button(text, command, frame):
    custom_button = TkinterCustomButton(master=frame,
                                        bg_color=None,
                                          fg_color="#212F3D",
                                          border_color="#117A65",
                                          hover_color="#34495E",
                                          text_font=None,
                                          text=text,
                                          text_color="white",
                                          corner_radius=12,
                                          border_width=4,
                                          width=120 if len(text) > 10 else 100,
                                          height=60,
                                          hover=True,
                                        command=command)
    return custom_button

def biseccion():
    biseccion_method_window(root)

def falsa_posicion():
    falsa_pocision_method_window(root)

def newton_raphson():
    newton_raphsonn_method_window(root)

def secante():
    secante_method_window(root)

root = tk.Tk()
root.title("Métodos Numericos")
root.configure(bg=color_fondo)  

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 600 
window_height = 300
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# Crear Frames para agrupar los botones por categoría
frame_cerrado = tk.Frame(root)
frame_cerrado.pack(side=tk.LEFT, padx=20, pady=10)
frame_cerrado.configure(bg=color_fondo)  

frame_abierto = tk.Frame(root)
frame_abierto.pack(side=tk.LEFT, padx=20, pady=10)
frame_abierto.configure(bg=color_fondo)  

frame_regresion = tk.Frame(root)
frame_regresion.pack(side=tk.LEFT, padx=20, pady=10)
frame_regresion.configure(bg=color_fondo)  

# Label para Métodos Cerrados
label_cerrados = tk.Label(frame_cerrado, text="Método Cerrados")
label_cerrados.pack(anchor=tk.NW)
label_cerrados.configure(bg=color_fondo)  

# Botones para Métodos Cerrados
bton_biseccion = create_custom_button("Biseccion", biseccion, frame_cerrado)
bton_biseccion.pack(pady=5)

bton_falsa_posicion = create_custom_button("Falsa Posición", falsa_posicion, frame_cerrado)
bton_falsa_posicion.pack(pady=5)

# Label para Métodos Abiertos
label_abiertos = tk.Label(frame_abierto, text="Método Abiertos")
label_abiertos.pack(anchor=tk.NW)
label_abiertos.configure(bg=color_fondo)  

# Botones para Métodos Abiertos
bton_newton_rap = create_custom_button("Newton Raphson", newton_raphson, frame_abierto)
bton_newton_rap.pack(pady=5)

bton_secante = create_custom_button("Secante", secante, frame_abierto)
bton_secante.pack(pady=5)

# Label para Regresion
frame_regresion = tk.Label(frame_regresion, text="Regresion")
frame_regresion.pack(anchor=tk.NW)
frame_regresion.configure(bg=color_fondo)  


root.mainloop()

