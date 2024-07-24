import sympy as sp
from scipy.optimize import root
from graficas import *

from graficas import graficar_cerrados

def biseccion(xi, xu, mi_funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero):
    porcentaje_aprox = porcentaje_aprox / 100
    porcentaje_verdadero = porcentaje_verdadero / 100

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

        if abs(xr) < 1e-10:  # Evitar divisiones por cantidades muy pequeñas
            mensaje = "xr es demasiado pequeño, lo que podría llevar a una división por un número muy pequeño."
            return mensaje, None, pasadas, datos_iteraciones, None
        
        if fxr == 0:  # Evitar divisiones por cero
            mensaje = f"Raiz Encontrada: {xr}"
            archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
            return mensaje, xr, pasadas, datos_iteraciones, archivo_grafica

        fxi_x_fxr = fxi * fxr

        if pasadas > 1:
            error_aprox = xr - xr_ant
            if abs(xr) > 1e-10:  # Evitar divisiones por cantidades muy pequeñas
                error_porcentual = (error_aprox / xr) * 100
            else:
                mensaje = "xr es demasiado pequeño, lo que podría llevar a una división por un número muy pequeño."
                archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
                return mensaje, xi, pasadas, datos_iteraciones, archivo_grafica

        error_verdadero = valor_verdadero - xr
        if abs(valor_verdadero) > 1e-10:  # Evitar divisiones por cantidades muy pequeñas
            error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100
        else:
            mensaje = "El valor verdadero es demasiado pequeño, lo que podría llevar a una división por un número muy pequeño."
            return mensaje, None, pasadas, datos_iteraciones, None

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
            archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
            return mensaje, xi, pasadas, datos_iteraciones, archivo_grafica

        if abs(error_verdadero_porcentual) <= porcentaje_verdadero:
            mensaje = f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}"
            archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
            return mensaje, xi, pasadas, datos_iteraciones, archivo_grafica

        if pasadas > 1:
            if abs(error_porcentual) <= porcentaje_aprox:
                mensaje = f"Error aproximado alcanzado: {abs(error_porcentual)}"
                archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
                return mensaje, xi, pasadas, datos_iteraciones, archivo_grafica

        pasadas += 1

    mensaje = f"Iteraciones realizadas: {max_pasadas}"
    archivo_grafica = graficar_cerrados('x', funcion, xi, xu, xr)
    return mensaje, xi, max_pasadas, datos_iteraciones, archivo_grafica
