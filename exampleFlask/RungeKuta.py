from sympy import symbols, Function, sympify, lambdify,dsolve,solve
from graficas import *

def evaluarValores(differential_equation, x_value, y_value):
    x, y = symbols('x y')
    ode_expression = sympify(differential_equation)
    y_func = Function('y')(x)
    modified_ode_expression = ode_expression.replace(y, y_func)
    numeric_function = lambdify((x, y_func), modified_ode_expression, "numpy")
    result = numeric_function(x_value, y_value)
    
    return result

def rungeKuta(ecuacion, x0, y0, incog, h):
    crifras_redondeo = 7

    xi = x0
    yi = y0
    h_med = h / 2
    
    datos_iteraciones = []

    xs = []  
    ys_numericos = []  
    ys_analiticos = [] 

    x, y = symbols('x y')
    ode_expression = sympify(ecuacion)
    y_func = Function('y')(x)

    sol_analitica = dsolve(y_func.diff(x) - ode_expression, y_func)
    C1 = symbols('C1')
    const_integration = solve(sol_analitica.subs({x: x0, y_func: y0}), C1)[0]
    sol_analitica = sol_analitica.subs(C1, const_integration)
    sol_analitica_func = lambdify(x, sol_analitica.rhs, "numpy")
    numeric_function = lambdify((x, y), ode_expression, "numpy")

    while xi < incog:

        y_analitica = sol_analitica_func(xi)
        if not isinstance(y_analitica, float):
            y = symbols('y')
            resultado = y_analitica.subs(y, yi)
            y_analitica = resultado

        k1 = evaluarValores(ecuacion, xi, yi)
        
        k_p1 = xi + h_med
        k2_p2 = yi + h_med * k1
        k2 = evaluarValores(ecuacion, k_p1, k2_p2)
        
        k3_p2 = yi + h_med * k2
        k3 = evaluarValores(ecuacion, k_p1, k3_p2)
        
        k4_p1 = xi + h
        k4_p2 = yi + h * k3
        k4 = evaluarValores(ecuacion, k_p1, k4_p2)
        
        Yi1 = yi + (1/6) * (k1 + 2*k2 + 2*k3 + k4) * h

        error = abs(y_analitica - Yi1)

        datos_iteraciones.append({
            'xi': round(float(xi), crifras_redondeo),
            'yi': round(float(yi), crifras_redondeo),
            'k1': round(float(k1), crifras_redondeo),
            'k2': round(float(k2), crifras_redondeo),
            'k3': round(float(k3), crifras_redondeo),
            'k4': round(float(k4), crifras_redondeo),
            'Yi+1': round(float(Yi1), crifras_redondeo),
            'y_analitica': round(float(y_analitica), crifras_redondeo),
            'error': round(float(error), crifras_redondeo),
        })

        xs.append(xi)
        ys_numericos.append(Yi1)
        ys_analiticos.append(y_analitica)

        xi = round(xi + h, 2)
        yi = Yi1
    
    grafica = graficar_edos(xs, ys_numericos, ys_analiticos)
    mensaje = f"Valor estimado en {incog}: {yi}"
    return mensaje, datos_iteraciones, grafica
