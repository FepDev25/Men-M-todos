import numpy as np
from scipy.interpolate import CubicSpline
from graficas import graficar_trazadores_cuadraticos

def calcular_trazadores_cuadraticos(x_data, y_data):
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)

    # Verificación de datos de entrada
    if len(x_data) != len(y_data):
        raise ValueError("Los datos de X e Y deben tener la misma longitud.")
    
    if len(x_data) < 3:
        raise ValueError("Se necesitan al menos 3 puntos para calcular los trazadores cuadráticos.")

    # Cálculo de los trazadores cuadráticos
    splines = []
    n = len(x_data) - 1
    a = y_data[:-1]
    h = np.diff(x_data)

    # Sistema de ecuaciones para obtener c
    A = np.zeros((n+1, n+1))
    b = np.zeros(n+1)

    A[0, 0] = 1
    A[n, n] = 1

    for i in range(1, n):
        A[i, i-1] = h[i-1]
        A[i, i] = 2 * (h[i-1] + h[i])
        A[i, i+1] = h[i]
        b[i] = 3 * ((y_data[i+1] - y_data[i]) / h[i] - (y_data[i] - y_data[i-1]) / h[i-1])

    c = np.linalg.solve(A, b)

    for i in range(n):
        b_i = (y_data[i+1] - y_data[i]) / h[i] - h[i] * (c[i+1] + 2 * c[i]) / 3
        d_i = (c[i+1] - c[i]) / (3 * h[i])
        splines.append({
            'a': a[i],
            'b': b_i,
            'c': c[i],
            'x0': x_data[i]
        })

    grafica = graficar_trazadores_cuadraticos(x_data, y_data, splines)
    mensaje = "Cálculo de trazadores cuadráticos completado exitosamente."

    return mensaje, splines, grafica
