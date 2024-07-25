import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from graficas import *

def extrapolacion_richardson(funcion_x, x0, h1, h2):
    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)

    x1 = x0 + h1
    x2 = x0 - h1
    eval1 = funcion.subs(x, x1)
    eval2 = funcion.subs(x, x2)

    first = ((eval1 - eval2))/(2*h1)

    x3 = x0 + h2
    x4 = x0 - h2
    eval3 = funcion.subs(x, x3)
    eval4 = funcion.subs(x, x4)

    second = ((eval3 - eval4))/(2*h2)

    third = (4/3)*second - (1/3)*first

    mensaje = f"Derivada calculada usando extrapolación de Richardson: {third}"

    derivada_analitica = sp.diff(funcion, x).subs(x, x0).evalf()
    error = abs(third - derivada_analitica)

    puntos_x = [x0]
    puntos_y = [funcion.subs(x, xi) for xi in puntos_x]
    archivo_grafica = graficar_derivada(x0, h1, h2, funcion, puntos_x, puntos_y, 'Derivada con extrapolación de Richardson', third, derivada_analitica)

    return mensaje, float(third), float(derivada_analitica), float(error), archivo_grafica
