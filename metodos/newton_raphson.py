import sympy as sp
import math

def newton_raphson(funcion_x, limite_iteraciones, x_inicial, porcentaje_error):
    x_n_1 = 0
    x_n = x_inicial
    x = sp.Symbol('x')
    funcion = funcion_x
    f_prima = sp.diff(funcion, x)
    funcion_derivada = f_prima
    iteracion = 1
    print(f"x{iteracion}: {x_n}")
    print()

    while iteracion <= limite_iteraciones:
        iteracion += 1
        x_n_1 = x_n

        f_xn = funcion.subs(x, x_n)
        f_dxn = funcion_derivada.subs(x, x_n)
        print(f"{x_n} evaluado en la funcion: {f_xn.evalf()}")
        print(f"{x_n} evaluado en la derivada: {f_dxn.evalf()}")

        x_n = (x_n - (f_xn/f_dxn)).evalf()

        error_aproximado = x_n - x_n_1
        error_aproximado_porcentual = (error_aproximado / x_n) * 100
        print(f"x{iteracion}: {x_n}")
        print(f"Error aproximado porcentual: {abs(error_aproximado_porcentual)}")

        if (abs(error_aproximado_porcentual) <= porcentaje_error):
            print(F"Error de {porcentaje_error}% alcanzado.")
            return x_n
        
        print()
    return x_n

valor_inicial = 9.5
x = sp.Symbol('x')
funcion = ((0.35 * math.e**(0.75*x)) / x) - 50
raiz = newton_raphson(funcion, 10, valor_inicial, 0.00006)
print(f"La raiz es {raiz}")
