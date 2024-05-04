import tkinter as tk
from biseccion import *
from falsa_pocision import *
from newton_raphson import *
from secante import *

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

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 500 
window_height = 300
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x, y))

# Metodos Cerrados
frame_cerrado = tk.Frame(root)
frame_cerrado.pack(pady=10)

label_cerrados = tk.Label(frame_cerrado, text="Método Cerrados")
label_cerrados.pack()

bton_biseccion = tk.Button(frame_cerrado, text="Biseccion", command=biseccion)
bton_biseccion.pack(pady=5)

bton_falsa_posicion = tk.Button(frame_cerrado, text="Falsa Posición", command=falsa_posicion)
bton_falsa_posicion.pack(pady=5)

# Metodos Abiertos
frame_abierto = tk.Frame(root)
frame_abierto.pack(pady=10)

label_abiertos = tk.Label(frame_abierto, text="Método Abiertos")
label_abiertos.pack()

bton_newton_rap = tk.Button(frame_abierto, text="Newton Raphson", command=newton_raphson)
bton_newton_rap.pack(pady=5)

bton_secante = tk.Button(frame_abierto, text="Secante", command=secante)
bton_secante.pack(pady=5)

root.mainloop()
