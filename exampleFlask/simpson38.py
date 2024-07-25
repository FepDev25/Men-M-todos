import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
from graficas import graficar_simpson

def simpson_tres_octavos(funcion_x, a, b, n):
    if n % 3 != 0:
        mensaje = "El número de subintervalos n debe ser múltiplo de 3"

    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)
    h = (b - a) / n

    suma = funcion.subs(x, a) + funcion.subs(x, b)

    for i in range(1, n):
        xi = a + i * h
        coeficiente = 3 if i % 3 != 0 else 2
        suma += coeficiente * funcion.subs(x, xi)

    area = (3 * h / 8) * suma
    area = area.evalf()
    mensaje = f"Área calculada usando la regla de Simpson 3/8: {area}"
    puntos_x = [a + i * h for i in range(n + 1)]
    puntos_y = [funcion.subs(x, xi) for xi in puntos_x]
    archivo_grafica = graficar_simpson(a, b, funcion, puntos_x, puntos_y, 'Aproximacion con simpson 3/8')

    integral_analitica = sp.integrate(funcion, (x, a, b)).evalf()
    error = abs(area - integral_analitica)

    return mensaje, float(area), archivo_grafica, float(integral_analitica), float(error)

