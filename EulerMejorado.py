from sympy import symbols, Function, sympify, lambdify

def evaluarValores(differential_equation, x_value, y_value):
    x, y = symbols('x y')    
    ode_expression = sympify(differential_equation)    
    y_func = Function('y')(x)    
    modified_ode_expression = ode_expression.replace(y, y_func)    
    numeric_function = lambdify((x, y_func), modified_ode_expression, "numpy")    
    result = numeric_function(x_value, y_value)
    
    return result

def eulerMetodo(ecuacion, x0, y0, incog, h):
    xi = x0
    yi = y0
    Yi1 = 0
    
    while xi < incog:
        
        i_evaluado = evaluarValores(ecuacion, xi, yi)
        
        Yn_1_elv = yi + h * i_evaluado
        
        Xn_1 = xi + h
        
        i_evaluado_2 = evaluarValores(ecuacion, Xn_1, Yn_1_elv)
        
        Yi1 = yi + (h/2) * (i_evaluado +  i_evaluado_2)
        
        print(f"xi={xi} - yi={yi}")
        print(f"Yi+1={Yi1}")
        print()
        
        xi = round(xi+h, 2)
        yi = Yi1
    
    print(f"xi={xi} - yi={yi}")
        
    return Yi1

ecuacion = "-2*x**3 + 12*x**2 - 20*x + 8.5"

x0 = 0
y0 = 1
incog = 1
h = 0.1

resultado = eulerMetodo(ecuacion, x0, y0, incog, h)