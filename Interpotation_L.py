import numpy as np

def polinomio_lagrange(x, y, x_estimado):
    n = len(x)
    resultado = 0.0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term *= (x_estimado - x[j]) / (x[i] - x[j])
        resultado += term
    return resultado


# Datos prueba
x = np.array([8, 9, 11])
f = np.log10(np.array([3, 6, 19]))

x_estimado = 10
log = polinomio_lagrange(x, f, x_estimado )
print(f"Log(10) estimado: {log}")
