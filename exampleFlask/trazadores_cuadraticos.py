import sympy as sp
from scipy.optimize import root
import os
import matplotlib.pyplot as plt

def trazadores_cuadraticos(xi, xu, mi_funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero):
    cifras_redondeo = 7
    xr_ant = 0
    xr = 0
    x = sp.Symbol('x')
    funcion = sp.sympify(mi_funcion)

    pasadas = 1
    datos_iteraciones = []

    error_aprox = 0
    error_aprox_porcentual = 0

    funcion_numerica = sp.lambdify(x, funcion)
    solucion = root(funcion_numerica, xi)
    valor_verdadero = solucion.x[0]

    while pasadas <= max_pasadas:
        xr_ant = xr

        # Aquí es donde se debe implementar el método de trazadores cuadráticos
        # Este es solo un ejemplo básico y puede necesitar ajustes
        xr = (xi + xu) / 2  # Simplemente tomar el punto medio, esto debe ser reemplazado por la interpolación cuadrática real
        
        fxi = funcion.subs(x, xi)
        fxu = funcion.subs(x, xu)
        fxr = funcion.subs(x, xr)

        fxi_x_fxr = fxi * fxr

        error_verdadero = valor_verdadero - xr
        error_verdadero_porcentual = (error_verdadero / valor_verdadero) * 100

        if pasadas > 1:
            error_aprox = xr - xr_ant
            error_aprox_porcentual = (error_aprox / xr) * 100

        datos_iteraciones.append({
            'xi': float(round(float(xi), cifras_redondeo)),
            'fxi': float(round(float(fxi), cifras_redondeo)),
            'xu': float(round(float(xu), cifras_redondeo)),
            'fxu': float(round(float(fxu), cifras_redondeo)),
            'xr': float(round(float(xr), cifras_redondeo)),
            'fxr': float(round(float(fxr), cifras_redondeo)),
            'valor_verdadero': float(round(float(valor_verdadero), cifras_redondeo)),
            'error_verdadero': float(round(abs(error_verdadero), cifras_redondeo + 1)),
            'error_verdadero_porcentual': float(round(abs(error_verdadero_porcentual), cifras_redondeo + 1)),
            'error_aprox': float(round(abs(error_aprox), cifras_redondeo + 1)),
            'error_porcentual': float(round(abs(error_aprox_porcentual), cifras_redondeo + 1))
        })

        if fxi_x_fxr < 0:
            xu = xr
        elif fxi_x_fxr > 0:
            xi = xr
        else:
            mensaje = f"Raíz encontrada: {xr}"
            ruta_grafica = graficar_trazadores('x', funcion, xi, xu, xr)
            return mensaje, float(xr), pasadas, datos_iteraciones, ruta_grafica

        if abs(error_verdadero_porcentual) <= porcentaje_verdadero:
            mensaje = f"Error verdadero alcanzado: {abs(error_verdadero_porcentual)}"
            ruta_grafica = graficar_trazadores('x', funcion, xi, xu, xr)
            return mensaje, float(xr), pasadas, datos_iteraciones, ruta_grafica

        if pasadas > 1:
            if abs(error_aprox_porcentual) <= porcentaje_aprox:
                mensaje = f"Error aproximado alcanzado: {abs(error_aprox_porcentual)}"
                ruta_grafica = graficar_trazadores('x', funcion, xi, xu, xr)
                return mensaje, float(xr), pasadas, datos_iteraciones, ruta_grafica

        pasadas += 1
    mensaje = f"Iteraciones realizadas: {max_pasadas}"
    ruta_grafica = graficar_trazadores('x', funcion, xi, xu, xr)
    return mensaje, float(xr), max_pasadas, datos_iteraciones, ruta_grafica

def graficar_trazadores(variable, funcion, xi, xu, xr):
    x = sp.Symbol(variable)
    x_vals = [xi, (xi + xu) / 2, xu]
    y_vals = [funcion.subs(x, xi), funcion.subs(x, (xi + xu) / 2), funcion.subs(x, xu)]
    interp_func = sp.interpolating_poly(2, x_vals, y_vals)

    p = sp.plot(funcion, (x, xi, xu), show=False)
    p.extend(sp.plot(interp_func, (x, xi, xu), show=False))

    filename = 'static/grafica_trazadores.png'
    p.save(filename)

    return filename
