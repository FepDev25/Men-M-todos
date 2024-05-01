import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tabla import Table

def biseccion(xi, xu, mi_funcion, max_pasadas, porcentaje_error):
    xr = 0
    xr_ant = 0
    x = sp.Symbol('x')
    funcion = mi_funcion

    pasadas = 1;
    datos_iteraciones = []

    while pasadas < max_pasadas:
        xr_ant = xr

        xr = (xi + xu) / 2
        
        fxi = funcion.subs(x, xi)
        fxu = funcion.subs(x, xu)
        fxr = funcion.subs(x, xr)

        fxi_x_fxr = fxi * fxr

        if fxi_x_fxr < 0:
            xu = xr
        elif fxi_x_fxr > 0:
            xi = xr
        else:
            return xr, pasadas, datos_iteraciones

        error_aprox = xr - xr_ant
        error_porcentual = (error_aprox / xr) * 100

        datos_iteraciones.append({
            'xi': xi,
            'fxi': fxi,
            'xu': xu,
            'fxu': fxu,
            'xr': xr,
            'fxr': fxr,
            'fxi_x_fxr': fxi_x_fxr,
            'error_aprox': abs(error_aprox),
            'error_porcentual': abs(error_porcentual)
        })

        if (abs(error_porcentual) <= porcentaje_error):
            return xr, pasadas, datos_iteraciones
        
        pasadas += 1
    return xr, pasadas, datos_iteraciones

def graficar_biseccion(simbolo, mi_funcion, rango_x, rango_y, raiz):
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_x, rango_y, 100)
    y_vals = funcion_numpy(x_vals)

    plt.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de $f(x)$')
    plt.scatter(raiz, 0, color='red')
    plt.grid(True)
    plt.legend()
    plt.show()

def biseccion_method_window(root):
    window = tk.Toplevel(root)
    window.title("Datos para Método de Bisección")

    label_funcion = tk.Label(window, text="Ingrese la función en términos de x: ")
    label_funcion.grid(row=0, column=0)
    entrada_funcion = tk.Entry(window)
    entrada_funcion.grid(row=0, column=1)

    label_xi = tk.Label(window, text="Ingrese el límite xi: ")
    label_xi.grid(row=1, column=0)
    entrada_xi = tk.Entry(window)
    entrada_xi.grid(row=1, column=1)

    label_xu = tk.Label(window, text="Ingrese el límite xu: ")
    label_xu.grid(row=2, column=0)
    entrada_xu = tk.Entry(window)
    entrada_xu.grid(row=2, column=1)

    label_iteraciones = tk.Label(window, text="Ingrese el número máximo de iteraciones: ")
    label_iteraciones.grid(row=3, column=0)
    entrada_iteraciones = tk.Entry(window)
    entrada_iteraciones.grid(row=3, column=1)

    label_error = tk.Label(window, text="Ingrese el porcentaje de error que desea manejar: ")
    label_error.grid(row=4, column=0)
    entrada_error = tk.Entry(window)
    entrada_error.grid(row=4, column=1)

    boton_calcular = tk.Button(window, text="Calcular", command=lambda: calcular_biseccion(
        entrada_funcion.get(), entrada_xi.get(), entrada_xu.get(), entrada_iteraciones.get(), entrada_error.get(), root, window))
    boton_calcular.grid(row=5, columnspan=2, pady=5)

def calcular_biseccion(funcion, xi, xu, iteraciones, error, root, window):
    xi = float(xi)
    xu = float(xu)
    iteraciones = int(iteraciones)
    error = float(error)

    funcion_expr = sp.sympify(funcion)

    raiz, pasadas, datos_iteraciones = biseccion(xi, xu, funcion_expr, iteraciones, error)

    table_window = tk.Toplevel(root)
    table_window.title("Tabla de Resultados")

    table = Table(table_window, filas=pasadas+1, columnas=9)
    table.pack(expand=True, fill=tk.BOTH)
    table.set_cell_value(0, 0, "xi")
    table.set_cell_value(0, 1, "f(xi)")
    table.set_cell_value(0, 2, "xu")
    table.set_cell_value(0, 3, "f(xu)")
    table.set_cell_value(0, 4, "xr")
    table.set_cell_value(0, 5, "f(xr)")
    table.set_cell_value(0, 6, "f(xi) * f(xu)")
    table.set_cell_value(0, 7, "error Aprx")
    table.set_cell_value(0, 8, "error Aprx %")

    for i, datos in enumerate(datos_iteraciones, start=1): 
        table.set_cell_value(i, 0, datos['xi'])
        table.set_cell_value(i, 1, datos['fxi'])
        table.set_cell_value(i, 2, datos['xu'])
        table.set_cell_value(i, 3, datos['fxu'])
        table.set_cell_value(i, 4, datos['xr'])
        table.set_cell_value(i, 5, datos['fxr'])
        table.set_cell_value(i, 6, datos['fxi_x_fxr'])
        table.set_cell_value(i, 7, datos['error_aprox'])
        table.set_cell_value(i, 8, datos['error_porcentual'])

    graficar_biseccion('x', funcion_expr, xi, xu, raiz)

    window.destroy()

