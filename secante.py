import sympy as sp
import tkinter as tk
from tabla import Table
from scipy.optimize import root
from tkinter import messagebox
from graficas import graficar_abiertos

def secante(mi_funcion, x0, x1, maximo_iteraciones, error_porcentaje_max, error_verdadero_max):
    iteracion = 1
    x = sp.Symbol('x')
    funcion = mi_funcion
    x_i = 0
    x_i_ant = 0
    error_aprox = 0
    error_aprox_porcentual = 0

    datos_iteraciones = []

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, x0) 
    valor_verdadero = solucion.x[0]

    while(iteracion <= maximo_iteraciones):
        x_i_ant = x_i

        fxi_1 = (funcion.subs(x, x1)).evalf()
        fxi_2 = (funcion.subs(x, x0)).evalf()    
        x_i = (x1 - (fxi_1 * (x1 - x0)) / (fxi_1 - fxi_2)).evalf()
        fxi = (funcion.subs(x, x_i)).evalf()

        error_verdadero = valor_verdadero - x_i
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        if (iteracion > 1):
            error_aprox = x_i_ant - x_i
            error_aprox_porcentual = (error_aprox / x_i) * 100

        cifras_redondeo = 7
        datos_iteraciones.append({
            'x0': round(x0, cifras_redondeo),
            'fx0': round(fxi_1, cifras_redondeo),
            'x1': round(x1, cifras_redondeo),
            'fx1': round(fxi_2, cifras_redondeo),
            'xi': x_i,
            'valor_verdadero': valor_verdadero,
            'error_verdadero': round(abs(error_verdadero),cifras_redondeo+1),
            'error_verdadero_porcentual': round(abs(error_verdadero_porcentual), cifras_redondeo+1), 
            'error_aprox':round( abs(error_aprox), cifras_redondeo+1),
            'error_aprox_porcentual': round(abs(error_aprox_porcentual), cifras_redondeo+1)
        })

        if (abs(error_verdadero_porcentual) <= error_verdadero_max):
            messagebox.showinfo("Raiz", f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}\nRaiz: {x_i}")
            return x_i, iteracion, datos_iteraciones
        
        if (iteracion > 1):
            if (abs(error_aprox_porcentual) <= error_porcentaje_max):
                messagebox.showinfo("Raiz", f"Error aproximado alcanzado: {abs(error_aprox_porcentual)}\nRaiz: {x_i}")
                return x_i, iteracion, datos_iteraciones


        x0 = x1
        x1 = x_i
        iteracion += 1
    return x_i, maximo_iteraciones, datos_iteraciones

def secante_method_window(root):
    window = tk.Toplevel(root)
    window.title("Datos para Método de la Secante")

    label_funcion = tk.Label(window, text="Ingrese la función en términos de x: ")
    label_funcion.grid(row=0, column=0)
    entrada_funcion = tk.Entry(window)
    entrada_funcion.grid(row=0, column=1)

    label_xi = tk.Label(window, text="Ingrese el valor de  X0: ")
    label_xi.grid(row=1, column=0)
    entrada_xi = tk.Entry(window)
    entrada_xi.grid(row=1, column=1)

    label_xu = tk.Label(window, text="Ingrese el valor de  X1: ")
    label_xu.grid(row=2, column=0)
    entrada_xu = tk.Entry(window)
    entrada_xu.grid(row=2, column=1)

    label_iteraciones = tk.Label(window, text="Ingrese el número máximo de iteraciones: ")
    label_iteraciones.grid(row=3, column=0)
    entrada_iteraciones = tk.Entry(window)
    entrada_iteraciones.grid(row=3, column=1)

    label_error_aprox = tk.Label(window, text="Ingrese el porcentaje de error aproximado que desea manejar: ")
    label_error_aprox.grid(row=4, column=0)
    entrada_error_aprox = tk.Entry(window)
    entrada_error_aprox.grid(row=4, column=1)

    label_error_verdadero = tk.Label(window, text="Ingrese el porcentaje de error verdadero que desea manejar: ")
    label_error_verdadero.grid(row=5, column=0)
    entrada_error_verdadero = tk.Entry(window)
    entrada_error_verdadero.grid(row=5, column=1)

    boton_calcular = tk.Button(window, text="Calcular", command=lambda: calcular_secante(
        entrada_funcion.get(), entrada_xi.get(), entrada_xu.get(), entrada_iteraciones.get(), entrada_error_aprox.get(), entrada_error_verdadero.get(),root, window))
    boton_calcular.grid(row=6, columnspan=2, pady=5)

def calcular_secante(mi_funcion, x0, x1, maximo_iteraciones, error_porcentaje_max, error_verdadero_max, root, window):
    if error_porcentaje_max == "":
        error_porcentaje_max = 0
    else:
        error_porcentaje_max = float(error_porcentaje_max)

    if error_verdadero_max == "":
        error_verdadero_max = 0
    else:
        error_verdadero_max = float(error_verdadero_max)

    x0 = float(x0)
    x1 = float(x1)
    iteraciones = int(maximo_iteraciones)

    funcion_expr = sp.sympify(mi_funcion)

    raiz, pasadas, datos_iteraciones = secante(funcion_expr, x0, x1, iteraciones, error_porcentaje_max, error_verdadero_max)

    table_window = tk.Toplevel(root)
    table_window.title("Tabla de Resultados")

    table = Table(table_window, filas=pasadas+1, columnas=11)
    table.pack(expand=True, fill=tk.BOTH)
    table.set_cell_value(0, 0, "Xi-2")
    table.set_cell_value(0, 1, "f(xi-2)")
    table.set_cell_value(0, 2, "Xi-1")
    table.set_cell_value(0, 3, "f(xi-1)")
    table.set_cell_value(0, 4, "Xi")
    table.set_cell_value(0, 5, "V Verd")
    table.set_cell_value(0, 6, "Err V")
    table.set_cell_value(0, 7, "Err V%")
    table.set_cell_value(0, 8, "Err Apr")
    table.set_cell_value(0, 9, "Err Apr%")

    for i, datos in enumerate(datos_iteraciones, start=1): 
        table.set_cell_value(i, 0, datos['x0'])
        table.set_cell_value(i, 1, datos['fx0'])
        table.set_cell_value(i, 2, datos['x1'])
        table.set_cell_value(i, 3, datos['fx1'])
        table.set_cell_value(i, 4, datos['xi'])
        table.set_cell_value(i, 5, datos['valor_verdadero'])
        table.set_cell_value(i, 6, datos['error_verdadero'])
        table.set_cell_value(i, 7, datos['error_verdadero_porcentual'])
        table.set_cell_value(i, 8, datos['error_aprox'])
        table.set_cell_value(i, 9, datos['error_aprox_porcentual'])

    graficar_abiertos('x', funcion_expr, int(raiz), raiz)