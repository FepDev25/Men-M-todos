import numpy as np
from scipy.interpolate import interp1d
from graficas import graficar_derivadas_irregulares

def calcular_derivadas_irregulares(pares, punto_estimar, metodo):
    x_data = np.array([p[0] for p in pares], dtype=float)
    y_data = np.array([p[1] for p in pares], dtype=float)
    
    if metodo not in ['central', 'adelante', 'atras']:
        raise ValueError("Método no válido. Use 'central', 'adelante' o 'atras'.")

    # Interpolación para los datos irregulares
    f = interp1d(x_data, y_data, kind='cubic', fill_value="extrapolate")

    # Método de diferencias finitas
    def diferencias_finitas(f, x, h, metodo):
        if metodo == 'central':
            return (f(x + h) - f(x - h)) / (2 * h)
        elif metodo == 'adelante':
            return (f(x + h) - f(x)) / h
        elif metodo == 'atras':
            return (f(x) - f(x - h)) / h

    # Estimación de la derivada en el punto dado
    h = np.min(np.diff(x_data))
    derivada = diferencias_finitas(f, punto_estimar, h, metodo)

    # Preparación de datos para la gráfica
    x_interpolado = np.linspace(np.min(x_data), np.max(x_data), 500)
    y_interpolado = f(x_interpolado)
    derivadas_interpoladas = [diferencias_finitas(f, x, h, metodo) for x in x_interpolado]

    # Genera la gráfica de la derivada
    grafica_path = graficar_derivadas_irregulares(x_interpolado, y_interpolado, derivadas_interpoladas)

    mensaje = f"Derivada estimada en x = {punto_estimar} usando el método {metodo}: {derivada}"
    resultado = {
        'x': x_interpolado.tolist(),
        'y': derivadas_interpoladas
    }

    return mensaje, resultado, grafica_path
