import matplotlib
matplotlib.use('Agg')  # Configura el backend para evitar problemas de GUI

import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import os

def graficar_cerrados(simbolo, mi_funcion, rango_izq, rango_der, raiz):
    rango_izq = float(rango_izq)
    rango_der = float(rango_der)
    raiz = float(raiz)
    
    rango_izq -= 10
    rango_der += 10

    x = sp.Symbol(simbolo)
    funcion = sp.sympify(mi_funcion)

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_izq, rango_der, 100)
    y_vals = funcion_numpy(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gráfico de $f(x)$')
    ax.scatter(raiz, 0, color='red')
    ax.grid(True)
    ax.legend()

    # Definir la ruta del archivo correctamente
    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica.png')

    # Eliminar el archivo si ya existe
    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    # Crear el directorio si no existe
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    # Guardar la gráfica en un archivo
    plt.savefig(archivo_grafica)
    plt.close(fig)

    return archivo_grafica


def graficar_abiertos(simbolo, mi_funcion, rango, raiz):
    rango = float(rango)
    raiz = float(raiz)

    x = sp.Symbol(simbolo)
    funcion = sp.sympify(mi_funcion)

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango - 10, rango + 10, 100)
    y_vals = funcion_numpy(x_vals)

    fig, ax = plt.subplots()
    ax.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.set_title('Gráfico de $f(x)$')
    ax.scatter(raiz, 0, color='red')
    ax.grid(True)
    ax.legend()

    # Definir la ruta del archivo correctamente
    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_abiertos.png')

    # Eliminar el archivo si ya existe
    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    # Crear el directorio si no existe
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    # Guardar la gráfica en un archivo
    plt.savefig(archivo_grafica)
    plt.close(fig)

    return archivo_grafica

# Método de gráfica para trazadores cuadráticos
def graficar_trazadores_cuadraticos(x_data, y_data, splines):
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, color='red', label='Datos')
    
    x_vals = np.linspace(min(x_data), max(x_data), 1000)
    y_vals = np.zeros_like(x_vals)
    
    for spline in splines:
        a = spline['a']
        b = spline['b']
        c = spline['c']
        x0 = spline['x0']
        
        for i in range(len(x_vals)):
            if x_vals[i] >= x0:
                y_vals[i] = a + b * (x_vals[i] - x0) + c * (x_vals[i] - x0) ** 2
    
    ax.plot(x_vals, y_vals, label='Trazador Cuadrático')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Trazadores Cuadráticos')
    ax.legend()
    ax.grid(True)
    
    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_trazadores_cuadraticos.png')

    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    plt.savefig(archivo_grafica)
    plt.close(fig)
    
    return archivo_grafica

def graficar_edos(xs, ys_numericos, ys_analiticos):
    fig, ax = plt.subplots()
    ax.plot(xs, ys_numericos, label='Solución Numérica', marker='o')
    ax.plot(xs, ys_analiticos, label='Solución Analítica', linestyle='--')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Comparación Solución Numérica vs. Analítica')
    ax.grid(True)
    ax.legend()

    # Definir la ruta del archivo correctamente
    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_euler.png')

    # Eliminar el archivo si ya existe
    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    # Crear el directorio si no existe
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    # Guardar la gráfica en un archivo
    plt.savefig(archivo_grafica)
    plt.close(fig)

    return archivo_grafica
