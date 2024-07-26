import numpy as np
import sympy as sp
from graficas import graficar_cuadratura_gauss

def cuadratura_gauss(funcion, a, b, n):
    x = sp.Symbol('x')
    f = sp.sympify(funcion)
    f_lambda = sp.lambdify(x, f, 'numpy')

    # Puntos y pesos para la cuadratura de Gauss-Legendre
    x_i, w_i = np.polynomial.legendre.leggauss(n)

    # Transformación de [-1, 1] a [a, b]
    x_trans = 0.5 * (b - a) * x_i + 0.5 * (b + a)
    
    # Cálculo de la integral
    integral = 0.5 * (b - a) * np.sum(w_i * f_lambda(x_trans))

    # Cálculo de la integral analítica para comparación
    integral_analitica = sp.integrate(f, (x, a, b))
    integral_analitica_valor = float(integral_analitica.evalf())

    # Cálculo del error
    error = abs(integral_analitica_valor - integral)

    # Generar gráfica
    archivo_grafica = graficar_cuadratura_gauss(f, a, b, x_trans, f_lambda(x_trans), integral)

    mensaje = f"La integral aproximada es: {integral:.6f}"
    return mensaje, integral, archivo_grafica, integral_analitica_valor, error