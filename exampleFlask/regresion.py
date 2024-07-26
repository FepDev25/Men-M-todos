import numpy as np
import matplotlib.pyplot as plt

def regresion(x, y, grado):
    coefficients = np.polyfit(x, y, grado)
    polinomio = np.poly1d(coefficients)
    
    x_new = np.linspace(min(x) - 1, max(x) + 1, 500)
    y_new = polinomio(x_new)
    
    return coefficients, polinomio, x_new, y_new

def formatear_polinomio(polinomio):
    terms = []
    for power, coef in enumerate(polinomio.coefficients[::-1]):
        if coef == 0:
            continue
        coef_str = f"{coef:+.4f}" if power > 0 else f"{coef:.4f}"
        if power == 0:
            terms.append(coef_str)
        elif power == 1:
            terms.append(f"{coef_str}x")
        else:
            terms.append(f"{coef_str}x^{power}")
    return " ".join(terms).replace("+-", "- ")

def plot_regresion(x, y, x_new, y_new, polinomio):
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color='blue', label='Datos originales')
    plt.plot(x_new, y_new, color='red', label='Línea de ajuste')
    plt.title(f'Regresión {("Lineal" if len(polinomio.coefficients) == 2 else "Polinomial")}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)
    plt.savefig('static/regresion_plot.png')
    plt.close()

def calcular_r_cuadrado(x, y, polinomio):
    y_pred = polinomio(x)
    ssr = np.sum((y - y_pred) ** 2)
    sst = np.sum((y - np.mean(y)) ** 2)
    r_squared = 1 - (ssr / sst)
    return r_squared

def calcular_regresion(x, y, tipo_regresion, grado=1):
    coefficients, polinomio, x_new, y_new = regresion(x, y, grado)
    ecuacion = formatear_polinomio(polinomio)
    plot_regresion(x, y, x_new, y_new, polinomio)
    r_squared = calcular_r_cuadrado(x, y, polinomio)
    
    return {
        'ecuacion': ecuacion,
        'r_squared': r_squared,
        'tipo_regresion': tipo_regresion,
        'grado': grado
    }