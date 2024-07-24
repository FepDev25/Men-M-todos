import sympy as sp
import tkinter as tk
from scipy.optimize import root
from graficas import graficar_abiertos

def secante(mi_funcion, x0, x1, maximo_iteraciones, error_porcentaje_max, error_verdadero_max):
    error_porcentaje_max = error_porcentaje_max / 100
    error_verdadero_max = error_verdadero_max / 100
    
    cifras_redondeo = 8
    iteracion = 1
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion)
    x_i = 0
    x_i_ant = 0
    error_aprox = 0
    error_aprox_porcentual = 0

    datos_iteraciones = []

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, x0) 
    valor_verdadero = solucion.x[0]

    while(iteracion <= maximo_iteraciones):
        x_i_ant = x_i

        fxi_1 = (funcion.subs(x, x1)).evalf()
        fxi_2 = (funcion.subs(x, x0)).evalf()    
        x_i = (x1 - (fxi_1 * (x1 - x0)) / (fxi_1 - fxi_2)).evalf()

        error_verdadero = valor_verdadero - x_i
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        if (iteracion > 1):
            error_aprox = x_i_ant - x_i
            error_aprox_porcentual = (error_aprox / x_i) * 100

        
        datos_iteraciones.append({
            'x0': round(float(x0), cifras_redondeo),
            'fx0': round(float(fxi_1), cifras_redondeo),
            'x1': round(float(x1), cifras_redondeo),
            'fx1': round(float(fxi_2), cifras_redondeo),
            'xi': round(float(x_i), cifras_redondeo+2),
            'valor_verdadero': round(float(valor_verdadero), cifras_redondeo+2),
            'error_verdadero': round(float(abs(error_verdadero)), cifras_redondeo),
            'error_verdadero_porcentual': round(float(abs(error_verdadero_porcentual)), cifras_redondeo),
            'error_aprox': round(float(abs(error_aprox)), cifras_redondeo),
            'error_aprox_porcentual': round(float(abs(error_aprox_porcentual)), cifras_redondeo)
        })

        if (abs(error_verdadero_porcentual) <= error_verdadero_max):
            mensaje = f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}"
            grafica = graficar_abiertos('x', funcion, int(x_i), x_i)
            return mensaje, float(x_i), iteracion, datos_iteraciones, grafica
        
        if (iteracion > 1):
            if (abs(error_aprox_porcentual) <= error_porcentaje_max):
                mensaje = f"Error aproximado alcanzado: {abs(error_aprox_porcentual)}"
                grafica = graficar_abiertos('x', funcion, int(x_i), x_i)
                return mensaje, float(x_i), iteracion, datos_iteraciones, grafica


        x0 = x1
        x1 = x_i
        iteracion += 1
    mensaje = f"Iteraciones realizadas: {maximo_iteraciones}"
    grafica = graficar_abiertos('x', funcion, int(x_i), x_i)
    return mensaje, float(x_i), iteracion, datos_iteraciones, grafica
