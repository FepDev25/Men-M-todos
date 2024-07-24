import numpy as np
import matplotlib.pyplot as plt

def derivadas_irregular(x_values, y_values):
    cifras_redondeo = 7

    x_values = np.array(x_values, dtype=float)
    y_values = np.array(y_values, dtype=float)

    n = len(x_values)
    derivadas = np.zeros(n)

    for i in range(1, n - 1):
        h1 = x_values[i] - x_values[i - 1]
        h2 = x_values[i + 1] - x_values[i]
        derivadas[i] = ((y_values[i + 1] - y_values[i]) / h2) - ((y_values[i] - y_values[i - 1]) / h1)
        derivadas[i] /= (h1 + h2) / 2

    derivadas[0] = (y_values[1] - y_values[0]) / (x_values[1] - x_values[0])
    derivadas[-1] = (y_values[-1] - y_values[-2]) / (x_values[-1] - x_values[-2])

    datos_iteraciones = []
    for i in range(n):
        datos_iteraciones.append({
            'x': float(round(x_values[i], cifras_redondeo)),
            'y': float(round(y_values[i], cifras_redondeo)),
            'derivada': float(round(derivadas[i], cifras_redondeo))
        })

    plt.figure()
    plt.plot(x_values, y_values, 'o', label='Datos')
    plt.plot(x_values, derivadas, '-', label='Derivadas')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x) y f\'(x)')
    plt.title('Derivadas de Datos Irregularmente Espaciados')

    grafica_path = 'static/derivadas_irregular.png'
    plt.savefig(grafica_path)
    plt.close()

    return "Cálculo completado", datos_iteraciones, grafica_path
