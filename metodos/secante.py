import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def secante(mi_funcion, x0, x1, maximo_iteraciones):
    
    iteracion = 1
    x = sp.Symbol('x')
    funcion = mi_funcion
    x_i = 0
    while(iteracion <= maximo_iteraciones):
        print(f"Iteracion N{iteracion}")
        print(f"x0: {x0}")
        print(f"x1: {x1}")

        fxi_1 = (funcion.subs(x, x1)).evalf()
        fxi_2 = (funcion.subs(x, x0)).evalf()
        print(f"f(Xi-1): {fxi_1}")
        print(f"f(Xi-2): {fxi_2}")
        
        x_i = (x1 - (fxi_1 * (x1 - x0)) / (fxi_1 - fxi_2)).evalf()
        print(f"xi: {x_i}")
        x0 = x1
        x1 = x_i

        fxi = (funcion.subs(x, x_i)).evalf()
        print(f"f(Xi): {fxi}")

        iteracion += 1
        print()
    return x_i

def graficar(simbolo, mi_funcion, rango_x, rango_y, raiz):
    x = sp.Symbol(simbolo)
    funcion = mi_funcion

    funcion_numpy = sp.lambdify(x, funcion, 'numpy')

    x_vals = np.linspace(rango_x, rango_y, 100)
    y_vals = funcion_numpy(x_vals)

    plt.plot(x_vals, y_vals, label=f'$f(x) = {str(funcion)}')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de $f(x)$')
    plt.scatter(raiz, 0, color='red')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    x = sp.Symbol('x')
    funcion = x**2  - 12
    raiz = secante(funcion, 2, 3, 5)
    graficar('x', funcion, 2, 4, raiz)