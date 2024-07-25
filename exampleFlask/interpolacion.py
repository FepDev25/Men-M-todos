import numpy as np
from scipy.interpolate import interp1d, CubicSpline, BSpline, splrep, splev, lagrange
import matplotlib.pyplot as plt
from graficas import *

def interpolacion_lineal(x, y, nuevos_x):
    f = interp1d(x, y, kind='linear')
    nuevos_y = f(nuevos_x)
    return nuevos_y

def interpolacion_splines_cubicos(x, y, nuevos_x):
    cs = CubicSpline(x, y)
    nuevos_y = cs(nuevos_x)
    return nuevos_y

def interpolacion_splines_bspline(x, y, nuevos_x, grado):
    tck = splrep(x, y, k=grado)
    nuevos_y = splev(nuevos_x, tck)
    return nuevos_y

def interpolacion_polinomios_lagrange(x, y, nuevos_x):
    poly = lagrange(x, y)
    nuevos_y = poly(nuevos_x)
    return nuevos_y


x = np.array([1, 2, 3, 4])
y = np.array([6, 1, -2, 7])
nuevos_x = np.array([1.5, 2.5, 3.31, 3.5])
nuevos_y = interpolacion_splines_cubicos(x,y,nuevos_x)
graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación Lineal')