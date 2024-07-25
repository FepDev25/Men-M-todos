import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import os
from graficas import graficar_simpson

def simpson_tercio(funcion_x, a, b, n):
    # Verificar que n es par
    if n % 2 != 0:
        raise ValueError("El número de subintervalos n debe ser par")

    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)
    h = (b - a) / n

    suma = funcion.subs(x, a) + funcion.subs(x, b)

    for i in range(1, n):
        xi = a + i * h
        coeficiente = 4 if i % 2 != 0 else 2
        suma += coeficiente * funcion.subs(x, xi)

    area = (h / 3) * suma
    area = area.evalf()
    mensaje = f"Área calculada usando la regla de Simpson 1/3: {area}"

    puntos_x = [a + i * h for i in range(n + 1)]
    puntos_y = [funcion.subs(x, xi) for xi in puntos_x]
    archivo_grafica = graficar_simpson(a, b, funcion, puntos_x, puntos_y, 'Aproximacion con metodo de Simpso 1/3')

    integral_analitica = sp.integrate(funcion, (x, a, b)).evalf()
    error = abs(area - integral_analitica)

    return mensaje, float(area), archivo_grafica, float(integral_analitica), float(error)