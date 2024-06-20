import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def regresion_window(master):
    def agregar_valores():
        try:
            x_val = float(entry_x.get())
            y_val = float(entry_y.get())
            entrada_x.insert(tk.END, x_val)
            entrada_y.insert(tk.END, y_val)
            entry_x.delete(0, tk.END)
            entry_y.delete(0, tk.END)
            error_label.config(text="")
        except ValueError:
            error_label.config(text="Ingrese valores numéricos válidos", fg="red")
    
    def formatear_polinomio(polinomio):
        terms = []
        for power, coef in enumerate(polinomio.coefficients[::-1]):
            if coef == 0:
                continue
            coef_str = f"{coef:+.2f}" if power > 0 else f"{coef:.2f}"
            if power == 0:
                terms.append(coef_str)
            elif power == 1:
                terms.append(f"{coef_str}x")
            else:
                terms.append(f"{coef_str}x^{power}")
        return " ".join(terms).replace("+-", "- ")

    def calcular_regresion():
        try:
            x = np.array([float(entrada_x.get(i)) for i in range(entrada_x.size())])
            y = np.array([float(entrada_y.get(i)) for i in range(entrada_y.size())])
            
            tipo_regresion = tipo_regresion_var.get()
            if tipo_regresion == "Lineal":
                grado = 1
            else:
                grado = int(grado_var.get())
            
            coefficients = np.polyfit(x, y, grado)
            polinomio = np.poly1d(coefficients)
            ecuacion.set(f"Función estimada: {formatear_polinomio(polinomio)}")
            
            x_new = np.linspace(min(x) - 10, max(x) + 10, 500)
            y_new = polinomio(x_new)
            
            ax.clear()
            ax.scatter(x, y, label='Datos originales')
            ax.plot(x_new, y_new, color='red', label='Línea de ajuste')
            ax.legend()
            canvas.draw()
            error_label.config(text="")
        except Exception as e:
            error_label.config(text=f"Error: {e}", fg="red")

    global ecuacion
    global canvas
    global ax
    
    window = tk.Toplevel(master)
    window.title("Regresión Polinomial")
    window.geometry('900x900')

    frame_entradas = tk.Frame(window)
    frame_entradas.pack(side=tk.TOP, pady=10)

    label_x = tk.Label(frame_entradas, text="Valores de X:")
    label_x.pack(side=tk.LEFT)
    entrada_x = tk.Listbox(frame_entradas, selectmode=tk.EXTENDED, width=10)
    entrada_x.pack(side=tk.LEFT)

    label_y = tk.Label(frame_entradas, text="Valores de Y:")
    label_y.pack(side=tk.LEFT)
    entrada_y = tk.Listbox(frame_entradas, selectmode=tk.EXTENDED, width=10)
    entrada_y.pack(side=tk.LEFT)

    frame_agregar = tk.Frame(window)
    frame_agregar.pack(side=tk.TOP, pady=10)

    label_nuevo_x = tk.Label(frame_agregar, text="Nuevo X:")
    label_nuevo_x.pack(side=tk.LEFT)
    entry_x = tk.Entry(frame_agregar, width=10)
    entry_x.pack(side=tk.LEFT)

    label_nuevo_y = tk.Label(frame_agregar, text="Nuevo Y:")
    label_nuevo_y.pack(side=tk.LEFT)
    entry_y = tk.Entry(frame_agregar, width=10)
    entry_y.pack(side=tk.LEFT)

    boton_agregar = tk.Button(frame_agregar, text="Agregar", command=agregar_valores)
    boton_agregar.pack(side=tk.LEFT)

    frame_opciones = tk.Frame(window)
    frame_opciones.pack(side=tk.TOP, pady=10)

    tipo_regresion_var = tk.StringVar()
    tipo_regresion_var.set("Lineal")
    radiobutton_lineal = tk.Radiobutton(frame_opciones, text="Lineal", variable=tipo_regresion_var, value="Lineal")
    radiobutton_lineal.pack(side=tk.LEFT)

    radiobutton_polinomial = tk.Radiobutton(frame_opciones, text="Polinomial", variable=tipo_regresion_var, value="Polinomial")
    radiobutton_polinomial.pack(side=tk.LEFT)

    grado_var = tk.StringVar()
    grado_var.set("2")
    label_grado = tk.Label(frame_opciones, text="Grado:")
    label_grado.pack(side=tk.LEFT)
    entrada_grado = tk.Spinbox(frame_opciones, from_=2, to=6, textvariable=grado_var, width=5)
    entrada_grado.pack(side=tk.LEFT)

    frame_grafica = tk.Frame(window)
    frame_grafica.pack(side=tk.TOP, pady=10)

    fig = Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
    canvas.get_tk_widget().pack()

    ecuacion = tk.StringVar()
    label_ecuacion = tk.Label(window, textvariable=ecuacion)
    label_ecuacion.pack(side=tk.TOP, pady=10)

    boton_calcular = tk.Button(window, text="Calcular", command=calcular_regresion)
    boton_calcular.pack(side=tk.TOP, pady=10)

    error_label = tk.Label(window, text="")
    error_label.pack(side=tk.TOP, pady=10)

    window.mainloop()

    

    
