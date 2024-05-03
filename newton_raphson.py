import math
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tabla import Table
from scipy.optimize import root
from tkinter import messagebox

def newton_raphson(funcion_x, limite_iteraciones, x_inicial, valor_error_aproximado, error_verdadero):
    x_n_1 = 0
    x_n = x_inicial
    x = sp.Symbol('x')
    funcion = funcion_x
    f_prima = sp.diff(funcion, x)
    funcion_derivada = f_prima
    iteracion = 1
    print(f"x{iteracion}: {x_n}")
    print()

    while iteracion <= limite_iteraciones:
        iteracion += 1
        x_n_1 = x_n

        f_xn = funcion.subs(x, x_n)
        f_dxn = funcion_derivada.subs(x, x_n)
        print(f"{x_n} evaluado en la funcion: {f_xn.evalf()}")
        print(f"{x_n} evaluado en la derivada: {f_dxn.evalf()}")

        x_n = (x_n - (f_xn/f_dxn)).evalf()

        error_aproximado = x_n - x_n_1
        error_aproximado_porcentual = (error_aproximado / x_n) * 100
        print(f"x{iteracion}: {x_n}")
        print(f"Error aproximado porcentual: {abs(error_aproximado_porcentual)}")

        if (abs(error_aproximado_porcentual) <= valor_error_aproximado):
            print(F"Error de {valor_error_aproximado}% alcanzado.")
            return x_n
        
        print()
    return x_n

def graficar_newton_raphson(simbolo, mi_funcion, rango, raiz):
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

def newton_raphsonn_method_window(root):
    pass

def calcular_newton_raphsonn(root):
    pass

"""valor_inicial = 9.5
x = sp.Symbol('x')
funcion = ((0.35 * math.e**(0.75*x)) / x) - 50
raiz = newton_raphson(funcion, 10, valor_inicial, 0.00006)
print(f"La raiz es {raiz}")"""