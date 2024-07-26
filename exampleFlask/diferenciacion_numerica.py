import numpy as np
import sympy as sp
from graficas import graficar_diferenciacion_numerica

def calcular_diferenciacion_numerica(funcion, intervalo, tamaño_paso, metodo):
    # Convertir la entrada
    x = sp.Symbol('x')
    func = sp.sympify(funcion)
    f = sp.lambdify(x, func, 'numpy')

    # Determinar el intervalo de evaluación
    intervalo = list(map(float, intervalo.split(',')))
    tamaño_paso = float(tamaño_paso)
    
    x_data = np.arange(intervalo[0], intervalo[1], tamaño_paso)
    y_data = f(x_data)

    # Método de diferenciación
    def diferencia_central(f, x, h):
        return (f(x + h) - f(x - h)) / (2 * h)
    
    if metodo == 'adelante':
        def diferencia_adicional(f, x, h):
            return (f(x + h) - f(x)) / h
        derivada = [diferencia_adicional(f, x, tamaño_paso) for x in x_data]
    
    elif metodo == 'atras':
        def diferencia_atras(f, x, h):
            return (f(x) - f(x - h)) / h
        derivada = [diferencia_atras(f, x, tamaño_paso) for x in x_data]
    
    elif metodo == 'central':
        derivada = [diferencia_central(f, x, tamaño_paso) for x in x_data]
    
    else:
        raise ValueError("Método no válido. Use 'adelante', 'atras', o 'central'.")

    mensaje = "Cálculo de la derivada completado exitosamente."

    # Genera la gráfica de la derivada
    grafica_path = graficar_diferenciacion_numerica(x_data, derivada)

    resultado = {
        'x': x_data.tolist(),
        'y': derivada,
        'grafica': grafica_path
    }

    return mensaje, resultado
