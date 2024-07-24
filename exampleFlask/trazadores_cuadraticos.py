import sympy as sp
from scipy.interpolate import interp1d
import numpy as np

import matplotlib.pyplot as plt

def trazadores_cuadraticos(xi, xu, mi_funcion, max_pasadas, porcentaje_aproximado, porcentaje_verdadero):
    cifras_redondeo = 7
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion)

    x_puntos = np.linspace(xi, xu, 10)
    y_puntos = [funcion.subs(x, punto) for punto in x_puntos]

    interpolacion = interp1d(x_puntos, y_puntos, kind='quadratic')

    datos_iteraciones = []
    valor_verdadero = y_puntos[-1]

    for i in range(len(x_puntos) - 1):
        xi = x_puntos[i]
        xu = x_puntos[i + 1]
        fx = interpolacion([xi, xu])

        error_verdadero = valor_verdadero - fx[1]
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100 if valor_verdadero != 0 else 0

        datos_iteraciones.append({
            'xi': float(round(xi, cifras_redondeo)),
            'fxi': float(round(fx[0], cifras_redondeo)),
            'xu': float(round(xu, cifras_redondeo)),
            'fxu': float(round(fx[1], cifras_redondeo)),
            'valor_verdadero': float(valor_verdadero),
            'error_verdadero': float(round(abs(error_verdadero), cifras_redondeo + 1)),
            'error_verdadero_porcentual': float(round(abs(error_verdadero_porcentual), cifras_redondeo + 1))
        })

    # Generar la gráfica
    plt.figure()
    plt.plot(x_puntos, y_puntos, 'o', label='Datos')
    plt.plot(x_puntos, interpolacion(x_puntos), '-', label='Trazador Cuadrático')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Trazadores Cuadráticos')

    # Guardar la gráfica en el directorio static
    grafica_path = 'static/trazador_cuadratico.png'
    plt.savefig(grafica_path)
    plt.close()

    return "Cálculo completado", xi, len(x_puntos) - 1, datos_iteraciones, grafica_path
