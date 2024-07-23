import sympy as sp
from scipy.optimize import root
from graficas import *

def biseccion(xi, xu, mi_funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero):
    cifras_redondeo = 7
    xr = 0
    xr_ant = 0
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion) 

    pasadas = 1
    datos_iteraciones = []

    error_aprox = 0
    error_porcentual = 0

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, xi)
    valor_verdadero = solucion.x[0]

    while pasadas <= max_pasadas:
        xr_ant = xr

        xr = (xi + xu) / 2
        
        fxi = funcion.subs(x, xi)
        fxu = funcion.subs(x, xu)
        fxr = funcion.subs(x, xr)

        fxi_x_fxr = fxi * fxr

        if pasadas > 1:
            error_aprox = xr - xr_ant
            error_porcentual = (error_aprox / xr) * 100

        error_verdadero = valor_verdadero - xr
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        
        datos_iteraciones.append({
            'xi': float(round(xi, cifras_redondeo)),
            'fxi': float(round(fxi, cifras_redondeo)),
            'xu': float(round(xu, cifras_redondeo)),
            'fxu': float(round(fxu, cifras_redondeo)),
            'xr': float(round(xr, cifras_redondeo)),
            'fxr': float(round(fxr, cifras_redondeo)),
            'valor_verdadero': float(valor_verdadero),
            'error_verdadero': float(round(abs(error_verdadero), cifras_redondeo + 1)),
            'error_verdadero_porcentual': float(round(abs(error_verdadero_porcentual), cifras_redondeo + 1)), 
            'error_aprox': float(round(abs(error_aprox), cifras_redondeo + 1)),
            'error_porcentual': float(round(abs(error_porcentual), cifras_redondeo + 1))
        })

        if fxi_x_fxr < 0:
            xu = xr
        elif fxi_x_fxr > 0:
            xi = xr
        else:
            mensaje = f"Raiz Encontrada: {xi}"
            return mensaje, xi, pasadas, datos_iteraciones

        if abs(error_verdadero_porcentual) <= porcentaje_verdadero:
            mensaje = f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}"
            return mensaje, xi, pasadas, datos_iteraciones

        if pasadas > 1:
            if abs(error_porcentual) <= porcentaje_aprox:
                mensaje = f"Error aproximado alcanzado: {abs(error_porcentual)}"
                return mensaje, xi, pasadas, datos_iteraciones

        pasadas += 1

    mensaje = f"Iteraciones realizadas: {max_pasadas}"
    return mensaje, xi, max_pasadas, datos_iteraciones
