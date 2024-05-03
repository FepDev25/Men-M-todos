import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tabla import Table
from scipy.optimize import root
from tkinter import messagebox
from graficas import graficar_abiertos

def newton_raphson(funcion_x, limite_iteraciones, x_inicial, valor_error_aproximado, valor_error_verdadero):
    x_n_1 = 0
    x_n = x_inicial
    x = sp.Symbol('x')
    funcion = funcion_x
    f_prima = sp.diff(funcion, x)
    funcion_derivada = f_prima
    iteracion = 1

    datos_iteraciones = []

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, x_inicial) 
    valor_verdadero = solucion.x[0]

    while iteracion <= limite_iteraciones:
        x_n_1 = x_n

        f_xn = funcion.subs(x, x_n)
        f_dxn = funcion_derivada.subs(x, x_n)

        x_n = (x_n - (f_xn/f_dxn)).evalf()

        error_aproximado = x_n - x_n_1
        error_aproximado_porcentual = (error_aproximado / x_n) * 100

        error_verdadero =  x_n - valor_verdadero
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        cifras_redondeo = 12
        datos_iteraciones.append({
            'Xi': round(x_n_1, cifras_redondeo),
            'Xi+1': round(x_n, cifras_redondeo),
            'valor_verdadero': valor_verdadero,
            'error_verdadero': round(abs(error_verdadero),cifras_redondeo),
            'error_verdadero_porcentual': round(abs(error_verdadero_porcentual), cifras_redondeo), 
            'error_aproximado':round( abs(error_aproximado), cifras_redondeo),
            'error_aproximado_prcentual': round(abs(error_aproximado_porcentual), cifras_redondeo)
        })

        if (abs(error_verdadero_porcentual) <= valor_error_verdadero):
            messagebox.showinfo("Raiz", f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}\nRaiz: {x_n}")
            return x_n, iteracion, datos_iteraciones
        if (abs(error_aproximado_porcentual) <= valor_error_aproximado):
            messagebox.showinfo("Raiz", f"Error aproximado alcanzado: {abs(error_aproximado_porcentual)}\nRaiz: {x_n}")
            return x_n, iteracion, datos_iteraciones
        
        iteracion += 1
    messagebox.showinfo("Raiz", f"Iteraciones realizadas: {limite_iteraciones}\nRaiz: {x_n}")
    return x_n, limite_iteraciones, datos_iteraciones

def newton_raphsonn_method_window(root):
    window = tk.Toplevel(root)
    window.title("Datos para Método de Newton Raphson")

    label_funcion = tk.Label(window, text="Ingrese la función en términos de x: ")
    label_funcion.grid(row=0, column=0)
    entrada_funcion = tk.Entry(window)
    entrada_funcion.grid(row=0, column=1)

    label_xn = tk.Label(window, text="Ingrese el valor para X inicial: ")
    label_xn.grid(row=1, column=0)
    entrada_xn = tk.Entry(window)
    entrada_xn.grid(row=1, column=1)

    label_iteraciones = tk.Label(window, text="Ingrese el número máximo de iteraciones: ")
    label_iteraciones.grid(row=2, column=0)
    entrada_iteraciones = tk.Entry(window)
    entrada_iteraciones.grid(row=2, column=1)

    label_error_aprox = tk.Label(window, text="Ingrese el porcentaje de error aproximado que desea manejar: ")
    label_error_aprox.grid(row=3, column=0)
    entrada_error_aprox = tk.Entry(window)
    entrada_error_aprox.grid(row=3, column=1)

    label_error_verdadero = tk.Label(window, text="Ingrese el porcentaje de error verdadero que desea manejar: ")
    label_error_verdadero.grid(row=4, column=0)
    entrada_error_verdadero = tk.Entry(window)
    entrada_error_verdadero.grid(row=4, column=1)

    boton_calcular = tk.Button(window, text="Calcular", command=lambda: calcular_newton_raphsonn(
        entrada_funcion.get(), entrada_xn.get(), entrada_iteraciones.get(), entrada_error_aprox.get(), entrada_error_verdadero.get(), root, window))
    boton_calcular.grid(row=5, columnspan=2, pady=5)

def calcular_newton_raphsonn(funcion, x_inicial, iteraciones_max, error_prox_max, error_verd_max, root, window):
    if error_prox_max == "":
        error_prox_max = 0
    else:
        error_prox_max = float(error_prox_max)

    if error_verd_max == "":
        error_verd_max = 0
    else:
        error_verd_max = float(error_verd_max)

    xn = float(x_inicial)
    iteraciones = int(iteraciones_max)

    funcion_expr = sp.sympify(funcion)

    raiz, pasadas, datos_iteraciones = newton_raphson(funcion_expr, iteraciones, xn, error_prox_max, error_verd_max)

    table_window = tk.Toplevel(root)
    table_window.title("Tabla de Resultados")

    table = Table(table_window, filas=pasadas+1, columnas=7)
    table.pack(expand=True, fill=tk.BOTH)
    table.set_cell_value(0, 0, "Xi")
    table.set_cell_value(0, 1, "Xi+1")
    table.set_cell_value(0, 2, "V Verd")
    table.set_cell_value(0, 3, "Err V")
    table.set_cell_value(0, 4, "Err V%")
    table.set_cell_value(0, 5, "Err Apr")
    table.set_cell_value(0, 6, "Err Apr%")

    for i, datos in enumerate(datos_iteraciones, start=1): 
        table.set_cell_value(i, 0, datos['Xi'])
        table.set_cell_value(i, 1, datos['Xi+1'])
        table.set_cell_value(i, 2, datos['valor_verdadero'])
        table.set_cell_value(i, 3, datos['error_verdadero'])
        table.set_cell_value(i, 4, datos['error_verdadero_porcentual'])
        table.set_cell_value(i, 5, datos['error_aproximado'])
        table.set_cell_value(i, 6, datos['error_aproximado_prcentual'])
    
    graficar_abiertos('x', funcion_expr, int(x_inicial), raiz)
    