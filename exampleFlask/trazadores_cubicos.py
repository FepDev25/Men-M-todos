import numpy as np
from scipy.interpolate import CubicSpline
from graficas import graficar_trazadores_cubicos

def calcular_trazadores_cubicos(x_data, y_data):
    x_data = np.array(x_data, dtype=float)
    y_data = np.array(y_data, dtype=float)

    # Verificación de datos de entrada
    if len(x_data) != len(y_data):
        raise ValueError("Los datos de X e Y deben tener la misma longitud.")
    
    if len(x_data) < 4:
        raise ValueError("Se necesitan al menos 4 puntos para calcular los trazadores cúbicos.")

    # Cálculo de los trazadores cúbicos usando scipy
    cs = CubicSpline(x_data, y_data, bc_type='natural')

    splines = []
    ecuaciones = []
    for i in range(len(x_data) - 1):
        a = cs.c[3, i]
        b = cs.c[2, i]
        c = cs.c[1, i]
        d = cs.c[0, i]
        x0 = x_data[i]

        spline_segment = {
            'a': a,
            'b': b,
            'c': c,
            'd': d,
            'x0': x0
        }
        splines.append(spline_segment)

        # Crear la ecuación como una cadena
        ecuacion = f"S{i}(x) = {a:.3f} + {b:.3f}(x - {x0:.3f}) + {c:.3f}(x - {x0:.3f})^2 + {d:.3f}(x - {x0:.3f})^3"
        ecuaciones.append(ecuacion)

    grafica = graficar_trazadores_cubicos(x_data, y_data, splines)
    mensaje = "Ecuaciones de los trazadores cúbicos:\n" + "\n".join(ecuaciones)

    return mensaje, splines, grafica
