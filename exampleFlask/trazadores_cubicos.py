import sympy as sp
from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt

def trazadores_cubicos(xi, xu, mi_funcion):
    cifras_redondeo = 7
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion)

    x_puntos = np.linspace(xi, xu, 10)
    y_puntos = [funcion.subs(x, punto) for punto in x_puntos]

    interpolacion = CubicSpline(x_puntos, y_puntos)

    datos_iteraciones = []

    for i in range(len(x_puntos) - 1):
        xi = x_puntos[i]
        xu = x_puntos[i + 1]
        fx = interpolacion([xi, xu])

        datos_iteraciones.append({
            'xi': float(round(xi, cifras_redondeo)),
            'fxi': float(round(fx[0], cifras_redondeo)),
            'xu': float(round(xu, cifras_redondeo)),
            'fxu': float(round(fx[1], cifras_redondeo))
        })

    plt.figure()
    plt.plot(x_puntos, y_puntos, 'o', label='Datos')
    plt.plot(x_puntos, interpolacion(x_puntos), '-', label='Trazador Cúbico')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Trazadores Cúbicos')

    grafica_path = 'static/trazador_cubico.png'
    plt.savefig(grafica_path)
    plt.close()

    return "Cálculo completado", datos_iteraciones, grafica_path
