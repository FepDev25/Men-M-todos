from sympy import symbols, Function, sympify, lambdify

def evaluarValores(differential_equation, x_value, y_value):
    x, y = symbols('x y')    
    ode_expression = sympify(differential_equation)    
    y_func = Function('y')(x)    
    modified_ode_expression = ode_expression.replace(y, y_func)    
    numeric_function = lambdify((x, y_func), modified_ode_expression, "numpy")    
    result = numeric_function(x_value, y_value)
    
    return result

def rungeKuta(ecuacion, x0, y0, incog, h):
    xi = x0
    yi = y0
    h_med = h/2
    Yi1 = 0
    
    while xi < incog:
        
        k1 = evaluarValores(ecuacion, xi, yi)
        
        k_p1 = xi + h_med
        k2_p2 = yi + h_med * k1
        k2 = evaluarValores(ecuacion, k_p1, k2_p2)
        
        k3_p2 = yi + h_med * k2
        k3 = evaluarValores(ecuacion, k_p1, k3_p2)
        
        k4_p1 = xi + h
        k4_p2 = yi + h * k3
        k4 = evaluarValores(ecuacion, k4_p1, k4_p2)
        
        Yi1 = yi +  (1/6) * (k1 + 2*k2 + 2*k3 + k4) * h
        
        print(f"xi={xi} - yi={yi}")
        print(f"k1={k1} - k2={k2} - k3={k3} - k4={k4}")
        print(f"Yi+1={Yi1}")
        print()
        
                
        xi = round(xi+h, 2)
        yi = Yi1
    
    print(f"xi={xi} - yi={yi}")
        
    return Yi1

ecuacion = "x * y**(1/2)"

x0 = 1
y0 = 4
incog = 1.6  
h = 0.1

resultado = rungeKuta(ecuacion, x0, y0, incog, h)