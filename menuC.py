from customtkinter import CTk, CTkFrame, CTkButton, CTkLabel
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

c_azul = '#7CCBEE'
c_azul_oscuro = '#034D92'
c_morado = '#7f5af0'
c_verde = '#2cb67d'
c_negro = '#000000'

root = CTk()

# Definir la función para centrar la ventana
def CenterWindowToDisplay(Screen, width, height, scale_factor=1.0):
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width / 2) - (width / 2)) * scale_factor)
    y = int(((screen_height / 2) - (height / 1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"

# Configurar la geometría de la ventana para que esté centrada
root.geometry(CenterWindowToDisplay(root, 500, 250, root._get_window_scaling()))
root.minsize(400,200)
root.config(bg=c_azul)
root.title("Métodos Numericos")

frame_cerrado = CTkFrame(root, fg_color=c_azul, border_color=c_verde, border_width=1)
frame_cerrado.grid(column=0, row=0, sticky='nsew', padx=50, pady=10)

label_cerrados = CTkLabel(frame_cerrado, text="Método Cerrados", bg_color=c_azul, fg_color=c_azul, text_color=c_negro, font=("Arial", 12, "bold"))
label_cerrados.pack(pady=10)

bton_biseccion = CTkButton(frame_cerrado, text="Bisección", command=biseccion, border_color=c_verde, fg_color=c_azul_oscuro, 
            hover_color=c_verde, corner_radius=12, border_width=2)
bton_biseccion.pack(pady=5)

bton_falsa_posicion = CTkButton(frame_cerrado, text="Falsa Posición", command=falsa_posicion, border_color=c_verde, fg_color=c_azul_oscuro, 
            hover_color=c_verde, corner_radius=12, border_width=2)
bton_falsa_posicion.pack(pady=5)

frame_abierto = CTkFrame(root, fg_color=c_azul, border_color=c_verde, border_width=1)
frame_abierto.grid(column=1, row=0, sticky='nsew', padx=50, pady=10)

label_abiertos = CTkLabel(frame_abierto, text="Método Abiertos", bg_color=c_azul, fg_color=c_azul, text_color=c_negro, font=("Arial", 12, "bold"))
label_abiertos.pack(pady=10)

bton_newton_rap = CTkButton(frame_abierto, text="Newton Raphson", command=newton_raphson, border_color=c_verde, fg_color=c_azul_oscuro, 
            hover_color=c_verde, corner_radius=12, border_width=2)
bton_newton_rap.pack(pady=5)

bton_secante = CTkButton(frame_abierto, text="Secante", command=secante, border_color=c_verde, fg_color=c_azul_oscuro, 
            hover_color=c_verde, corner_radius=12, border_width=2)
bton_secante.pack(pady=5)

root.mainloop()
