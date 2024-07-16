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
        
        Yi1 = yi +  i_evaluado * h
        
        print(f"xi={xi} - yi={yi}")
        print(f"Yi+1={Yi1}")
        print()
        
        xi = round(xi+h, 2)
        yi = Yi1
    
    print(f"xi={xi} - yi={yi}")
        
    return Yi1

ecuacion = "0.4 * x * y"

x0 = 1
y0 = 1
incog = 2
h = 0.1

resultado = eulerMetodo(ecuacion, x0, y0, incog, h)