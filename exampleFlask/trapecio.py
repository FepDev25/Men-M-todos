import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
from graficas import graficar_simpson

def metodo_trapecio(funcion_x, a, b, n):
    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)
    h = (b - a) / n

    suma = (funcion.subs(x, a) + funcion.subs(x, b)) / 2

    for i in range(1, n):
        xi = a + i * h
        suma += funcion.subs(x, xi)

    area = h * suma
    area = area.evalf()
    mensaje = f"Área calculada usando la regla del trapecio: {area}"

    puntos_x = [a + i * h for i in range(n + 1)]
    puntos_y = [funcion.subs(x, xi) for xi in puntos_x]
    archivo_grafica = graficar_simpson(a, b, funcion, puntos_x, puntos_y, 'Aproximacion con metodo del trapecio')

    integral_analitica = sp.integrate(funcion, (x, a, b)).evalf()
    error = abs(area - integral_analitica)

    return mensaje, float(area), archivo_grafica, float(integral_analitica), float(error)