import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

def diferenciacion_alta_precision(x0, h, mi_funcion):
    cifras_redondeo = 7
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion)

    funcion_derivada = sp.diff(funcion, x)
    funcion_lambdified = sp.lambdify(x, funcion)
    funcion_derivada_lambdified = sp.lambdify(x, funcion_derivada)

    f_x0 = funcion_lambdified(x0)
    f_x0_h = funcion_lambdified(x0 + h)
    f_x0_mh = funcion_lambdified(x0 - h)

    derivada_aproximada = (f_x0_h - f_x0_mh) / (2 * h)
    derivada_real = funcion_derivada_lambdified(x0)
    error = derivada_real - derivada_aproximada
    error_porcentual = (error / derivada_real) * 100 if derivada_real != 0 else 0

    datos_iteraciones = [{
        'x0': float(round(x0, cifras_redondeo)),
        'h': float(round(h, cifras_redondeo)),
        'derivada_aproximada': float(round(derivada_aproximada, cifras_redondeo)),
        'derivada_real': float(round(derivada_real, cifras_redondeo)),
        'error': float(round(abs(error), cifras_redondeo)),
        'error_porcentual': float(round(abs(error_porcentual), cifras_redondeo))
    }]

    # Generar la gráfica
    x_vals = np.linspace(x0 - h * 5, x0 + h * 5, 400)
    y_vals = funcion_lambdified(x_vals)
    y_derivada_vals = funcion_derivada_lambdified(x_vals)

    plt.figure()
    plt.plot(x_vals, y_vals, label='Función')
    plt.plot(x_vals, y_derivada_vals, label='Derivada Real')
    plt.scatter([x0], [derivada_aproximada], color='red', label='Derivada Aproximada')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x) y f\'(x)')
    plt.title('Diferenciación Numérica de Alta Precisión')

    grafica_path = 'static/diferenciacion_alta_precision.png'
    plt.savefig(grafica_path)
    plt.close()

    return "Cálculo completado", datos_iteraciones, grafica_path
