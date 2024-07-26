from sympy import symbols, Function, sympify, dsolve, lambdify, Eq, solve
import numpy as np
import matplotlib.pyplot as plt
from graficas import *

def euler_mejorado(ecuacion, x0, y0, incog, h):
    digitos_redondeo = 6
    xi = x0
    yi = y0

    datos_iteraciones = []

    xs = []
    ys_numericos = []
    ys_analiticos = []

    x, y = symbols('x y')
    y_func = Function('y')(x)
    ode_expression = sympify(ecuacion)

    # Definir la función para evaluar la ecuación diferencial
    numeric_function = lambdify((x, y_func), ode_expression, "numpy")
    
    # Resolver la ecuación diferencial analíticamente
    sol_analitica = dsolve(y_func.diff(x) - ode_expression, y_func)
    C1 = symbols('C1')
    const_integration = solve(sol_analitica.subs({x: x0, y_func: y0}), C1)[0]
    sol_analitica = sol_analitica.subs(C1, const_integration)
    sol_analitica_func = lambdify(x, sol_analitica.rhs, "numpy")

    while xi <= incog:
        # Evaluar la ecuación diferencial en el punto actual
        i_evaluado = numeric_function(xi, yi)
        
        # Método de Euler mejorado
        Yn_1_elv = yi + h * i_evaluado
        Xn_1 = xi + h
        i_evaluado_2 = numeric_function(Xn_1, Yn_1_elv)
        Yi1 = yi + (h/2) * (i_evaluado + i_evaluado_2)

        # Evaluar la solución analítica en xi
        y_analitica = sol_analitica_func(xi)
        if not isinstance(y_analitica, float):
            y = symbols('y')
            resultado = y_analitica.subs(y, yi)
            y_analitica = resultado
        else:
            y_analitica = round(float(resultado), digitos_redondeo)

        # Calcular el error
        error = abs(Yi1 - y_analitica)

        # Almacenar datos de iteración
        datos_iteraciones.append({
            'xi': round(float(xi), digitos_redondeo),
            'yi': round(float(yi), digitos_redondeo),
            'Yn_1_elv': Yn_1_elv,
            'Xn_1': round(float(Xn_1), digitos_redondeo),
            'Yi+1': round(float(Yi1), digitos_redondeo),
            'y_analitica': y_analitica,
            'error': round(float(error), digitos_redondeo)
        })

        xs.append(xi)
        ys_numericos.append(Yi1)
        ys_analiticos.append(y_analitica)

        xi = round(xi + h, 2)
        yi = Yi1

    grafica = graficar_edos(xs, ys_numericos, ys_analiticos)
    mensaje = f"Valor estimado en {incog}: {yi}"
    return mensaje, datos_iteraciones, grafica

