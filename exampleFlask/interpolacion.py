import numpy as np
from scipy.interpolate import interp1d, CubicSpline, BSpline, splrep, splev, lagrange
from graficas import *

def interpolacion_lineal(x, y, nuevos_x):
    f = interp1d(x, y, kind='linear')
    nuevos_y = f(nuevos_x)
    ruta_grafica = graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación Lineal')
    return x,y,nuevos_x,nuevos_y,ruta_grafica

def interpolacion_splines_cubicos(x, y, nuevos_x):
    cs = CubicSpline(x, y)
    nuevos_y = cs(nuevos_x)
    ruta_grafica = graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación Spline Cubico')
    return x,y,nuevos_x,nuevos_y,ruta_grafica

def interpolacion_splines_bspline(x, y, nuevos_x, grado):
    tck = splrep(x, y, k=grado)
    nuevos_y = splev(nuevos_x, tck)
    ruta_grafica = graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación con ajuste de grado')
    return x,y,nuevos_x,nuevos_y,ruta_grafica

def interpolacion_polinomios_lagrange(x, y, nuevos_x):
    poly = lagrange(x, y)
    nuevos_y = poly(nuevos_x)
    ruta_grafica = graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación de Lagrange')
    return x,y,nuevos_x,nuevos_y,ruta_grafica
