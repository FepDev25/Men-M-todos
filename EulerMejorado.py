import tkinter as tk
from tkinter import messagebox
from sympy import symbols, Function, sympify, lambdify
from tabla import Table

def evaluarValores(differential_equation, x_value, y_value):
    x, y = symbols('x y')    
    ode_expression = sympify(differential_equation)    
    y_func = Function('y')(x)    
    modified_ode_expression = ode_expression.replace(y, y_func)    
    numeric_function = lambdify((x, y_func), modified_ode_expression, "numpy")    
    result = numeric_function(x_value, y_value)
    
    return result

def eulerMetodo(ecuacion, x0, y0, incog, h, root):
    xi = x0
    yi = y0
    Yi1 = 0
    
    datos_iteraciones = []

    x = symbols('x')
    ode_expression = sympify(ecuacion)
    y_func = Function('y')(x)
    modified_ode_expression = ode_expression.replace(y_func, y_func)
    numeric_function = lambdify((x, y_func), modified_ode_expression, "numpy")

    while xi < incog:
        i_evaluado = numeric_function(xi, yi)
        
        Yn_1_elv = yi + h * i_evaluado
        Xn_1 = xi + h
        
        i_evaluado_2 = numeric_function(Xn_1, Yn_1_elv)
        
        Yi1 = yi + (h/2) * (i_evaluado +  i_evaluado_2)

        datos_iteraciones.append({
            'xi': xi,
            'yi': yi,
            'Yn_1_elv': Yn_1_elv,
            'Xn_1': Xn_1,
            'Yi+1': Yi1
        })

        xi = round(xi + h, 2)
        yi = Yi1

    table_window = tk.Toplevel(root)
    table_window.title("Tabla de Resultados")

    table = Table(table_window, filas=len(datos_iteraciones)+1, columnas=5)
    table.pack(expand=True, fill=tk.BOTH)
    table.set_cell_value(0, 0, "xi")
    table.set_cell_value(0, 1, "yi")
    table.set_cell_value(0, 2, "Y(Yn+1)*")
    table.set_cell_value(0, 3, "Xn+1")
    table.set_cell_value(0, 4, "Yi+1")

    for i, datos in enumerate(datos_iteraciones, start=1):
        table.set_cell_value(i, 0, datos['xi'])
        table.set_cell_value(i, 1, datos['yi'])
        table.set_cell_value(i, 2, datos['Yn_1_elv'])
        table.set_cell_value(i, 3, datos['Xn_1'])
        table.set_cell_value(i, 4, datos['Yi+1'])

    tk.messagebox.showinfo("Método de Euler Mejorado", f"Cálculo completado. Resultado final: {Yi1}")

def euler_mejorado_method_window(root):
    window = tk.Toplevel(root)
    window.title("Datos para Método de Euler Mejorado")

    label_ecuacion = tk.Label(window, text="Ingrese la ecuación diferencial: dy/dx=")
    label_ecuacion.grid(row=0, column=0)
    entrada_ecuacion = tk.Entry(window)
    entrada_ecuacion.grid(row=0, column=1)

    label_x0 = tk.Label(window, text="Ingrese el valor inicial de x (x0): ")
    label_x0.grid(row=1, column=0)
    entrada_x0 = tk.Entry(window)
    entrada_x0.grid(row=1, column=1)

    label_y0 = tk.Label(window, text="Ingrese el valor inicial de y (y0): ")
    label_y0.grid(row=2, column=0)
    entrada_y0 = tk.Entry(window)
    entrada_y0.grid(row=2, column=1)

    label_incog = tk.Label(window, text="Ingrese el valor hasta donde quiere llegar: ")
    label_incog.grid(row=3, column=0)
    entrada_incog = tk.Entry(window)
    entrada_incog.grid(row=3, column=1)

    label_h = tk.Label(window, text="Ingrese el tamaño del paso (h): ")
    label_h.grid(row=4, column=0)
    entrada_h = tk.Entry(window)
    entrada_h.grid(row=4, column=1)

    boton_calcular = tk.Button(window, text="Calcular", command=lambda: calcular_euler(
        entrada_ecuacion.get(), entrada_x0.get(), entrada_y0.get(), entrada_incog.get(), entrada_h.get(), root, window))
    boton_calcular.grid(row=5, columnspan=2, pady=5)

def calcular_euler(ecuacion, x0, y0, incog, h, root, window):
    try:
        x0 = float(x0)
        y0 = float(y0)
        incog = float(incog)
        h = float(h)

        eulerMetodo(ecuacion, x0, y0, incog, h, root)
    except ValueError:
        tk.messagebox.showwarning(title="Error", message="Ingresar Valores Válidos.")


ecuacion = "-2*x**3 + 12*x**2 - 20*x + 8.5"

x0 = 0
y0 = 1
incog = 1
h = 0.1