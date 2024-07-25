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

#Metodo graficar trazadores_cubicos
def graficar_trazadores_cubicos(x_data, y_data, splines):
    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, color='red', label='Datos')
    
    x_vals = np.linspace(min(x_data), max(x_data), 1000)
    y_vals = np.zeros_like(x_vals)
    
    for spline in splines:
        a = spline['a']
        b = spline['b']
        c = spline['c']
        d = spline['d']
        x0 = spline['x0']
        
        for i in range(len(x_vals)):
            if x_vals[i] >= x0:
                y_vals[i] = a + b * (x_vals[i] - x0) + c * (x_vals[i] - x0)**2 + d * (x_vals[i] - x0)**3
    
    ax.plot(x_vals, y_vals, label='Trazador Cúbico')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Trazadores Cúbicos')
    ax.legend()
    ax.grid(True)
    
    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_trazadores_cubicos.png')

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

def graficar_simpson(a, b, funcion_x, puntos_x, puntos_y, label):
    x = sp.Symbol('x')
    funcion = sp.sympify(funcion_x)
    funcion_lambdified = sp.lambdify(x, funcion)

    xs = np.linspace(a, b, 1000)
    ys = funcion_lambdified(xs)

    fig, ax = plt.subplots()
    ax.plot(xs, ys, label='Función Original', color='blue')
    ax.scatter(puntos_x, puntos_y, color='red')
    ax.plot(puntos_x, puntos_y, label=label, color='red', linestyle='--')
    ax.fill_between(xs, 0, ys, alpha=0.2, color='blue')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(label)
    ax.grid(True)
    ax.legend()

    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_simpson.png')

    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    plt.savefig(archivo_grafica)
    plt.close(fig)

    return archivo_grafica

def graficar_derivada(x0, h1, h2, funcion, puntos_x, puntos_y, titulo, pendiente_numerica, pendiente_analitica):
    x = sp.Symbol('x')
    funcion_lambdified = sp.lambdify(x, funcion, modules='numpy')

    x_vals = np.linspace(x0 - 2*max(h1, h2), x0 + 2*max(h1, h2), 400)
    y_vals = funcion_lambdified(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, label='Función original', color='blue')
    plt.scatter(puntos_x, puntos_y, color='red', zorder=5)
    for i, (px, py) in enumerate(zip(puntos_x, puntos_y)):
        plt.text(px, py, f'P{i+1}({px:.2f}, {py:.2f})')

    plt.axvline(x=x0, color='green', linestyle='--', label=f'x0 = {x0}')

    y0 = funcion.subs(x, x0)
    tangente_numerica = pendiente_numerica * (x_vals - x0) + y0
    plt.plot(x_vals, tangente_numerica, label='Recta tangente numérica', color='orange', linestyle='--')

    tangente_analitica = pendiente_analitica * (x_vals - x0) + y0
    plt.plot(x_vals, tangente_analitica, label='Recta tangente analítica', color='purple', linestyle='--')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)

    directorio_static = os.path.abspath(os.path.join(os.getcwd(), 'static'))
    archivo_grafica = os.path.join(directorio_static, 'grafica_derivada_richardson.png')

    if os.path.exists(archivo_grafica):
        os.remove(archivo_grafica)
    
    if not os.path.exists(directorio_static):
        os.makedirs(directorio_static)

    plt.savefig(archivo_grafica)
    plt.close()

    return archivo_grafica

def graficar_interpolacion(x, y, nuevos_x, nuevos_y, titulo='Interpolación'):
    plt.figure(figsize=(10, 6))
    
    x_total = np.concatenate((x, nuevos_x))
    y_total = np.concatenate((y, nuevos_y))
    
    orden_indices = np.argsort(x_total)
    x_total = x_total[orden_indices]
    y_total = y_total[orden_indices]
    
    plt.plot(x, y, 'o', label='Datos originales', color='blue')
    plt.plot(nuevos_x, nuevos_y, 'x', label='Valores interpolados', color='red')
    plt.plot(x_total, y_total, label='Valores Unidos', color='green', linestyle='-', marker='x')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(titulo)
    plt.legend()
    plt.grid(True)
    plt.show()
