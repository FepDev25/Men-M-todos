import math
import sympy as sp
import numpy as np
from scipy.optimize import root
from graficas import graficar_abiertos

def newton_raphson(funcion_x, limite_iteraciones, x_inicial, valor_error_aproximado, valor_error_verdadero):
    valor_error_aproximado = valor_error_aproximado / 100
    valor_error_verdadero = valor_error_verdadero / 100

    cifras_redondeo = 8
    x_n_1 = 0
    x_n = x_inicial
    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)
    f_prima = sp.diff(funcion, x)
    funcion_derivada = f_prima
    iteracion = 1

    datos_iteraciones = []

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, x_inicial) 
    valor_verdadero = solucion.x[0]

    while iteracion <= limite_iteraciones:
        x_n_1 = x_n

        f_xn = funcion.subs(x, x_n)
        f_dxn = funcion_derivada.subs(x, x_n)

        x_n = (x_n - (f_xn/f_dxn)).evalf()

        error_aproximado = x_n - x_n_1
        error_aproximado_porcentual = (error_aproximado / x_n) * 100

        error_verdadero =  x_n - valor_verdadero
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        
        datos_iteraciones.append({
            'Xi': round(float(x_n_1), cifras_redondeo),
            'Xi+1': round(float(x_n), cifras_redondeo),
            'valor_verdadero': float(valor_verdadero),
            'error_verdadero': round(float(abs(error_verdadero)), cifras_redondeo),
            'error_verdadero_porcentual': round(float(abs(error_verdadero_porcentual)), cifras_redondeo), 
            'error_aproximado': round(float(abs(error_aproximado)), cifras_redondeo),
            'error_aproximado_prcentual': round(float(abs(error_aproximado_porcentual)), cifras_redondeo)
        })

        if (abs(error_verdadero_porcentual) <= valor_error_verdadero):
            mensaje = f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}"
            grafica = graficar_abiertos('x', funcion, int(x_n), x_n)
            return mensaje, float(x_n), iteracion, datos_iteraciones, grafica
        if (abs(error_aproximado_porcentual) <= valor_error_aproximado):
            mensaje = f"Error aproximado alcanzado: {abs(error_aproximado_porcentual)}"
            grafica = graficar_abiertos('x', funcion, int(x_n), x_n)
            return mensaje, float(x_n), iteracion, datos_iteraciones, grafica
        
        iteracion += 1
    mensaje = f"Iteraciones realizadas: {limite_iteraciones}"
    grafica = graficar_abiertos('x', funcion, int(x_n), x_n)
    return mensaje, float(x_n), limite_iteraciones, datos_iteraciones, grafica
