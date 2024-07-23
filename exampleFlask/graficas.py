import matplotlib
matplotlib.use('Agg')  # Configura el backend para evitar problemas de GUI

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import os

def graficar_cerrados(simbolo, mi_funcion, rango_izq, rango_der, raiz):
    rango_izq = float(rango_izq - 10)
    rango_der= float(rango_der+10)
    x = sp.Symbol(simbolo)
    funcion = sp.sympify(mi_funcion)

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_izq, rango_der, 100)
    y_vals = funcion_numpy(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gráfico de $f(x)$')
    ax.scatter(raiz, 0, color='red')
    ax.grid(True)
    ax.legend()

    archivo_grafica = 'static/grafica.png'

    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
        
    if not os.path.exists('static'):
        os.makedirs('static')

    plt.savefig(archivo_grafica)
    plt.close(fig)

    return archivo_grafica



def graficar_abiertos(simbolo, mi_funcion, rango, raiz):
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango-10, rango+10, 100)
    y_vals = funcion_numpy(x_vals)

    plt.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de $f(x)$')
    plt.scatter(raiz, 0, color='red')
    plt.grid(True)
    plt.legend()
    plt.show()