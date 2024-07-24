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


def graficar_euler(xs, ys_numericos, ys_analiticos):
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

grafica = graficar_euler([1,2,3,4,5,6,7], [1,2,3,4,5,6,7], [1.1,2,3.5,4,5.5,6.6,7])
print(grafica)
if os.path.exists(grafica):
    print("existe")