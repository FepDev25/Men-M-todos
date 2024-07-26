import numpy as np
import matplotlib.pyplot as plt

def gauss_jordan(A, b):
    n = len(b)
    A = A.astype('float64')
    b = b.astype('float64')
    Ab = np.column_stack((A, b))  # Matriz aumentada
    steps = []

    for k in range(n):
        # Pivoteo parcial
        max_index = k + np.argmax(np.abs(Ab[k:, k]))
        if max_index != k:
            Ab[[k, max_index]] = Ab[[max_index, k]]
        
        steps.append({
            'step': f'Pivoteo en fila {k+1}',
            'Ab': Ab.tolist()
        })

        # Normalización de la fila pivote
        pivot = Ab[k, k]
        Ab[k] /= pivot

        steps.append({
            'step': f'Normalización de fila {k+1}',
            'Ab': Ab.tolist()
        })

        # Eliminación
        for i in range(n):
            if i != k:
                factor = Ab[i, k]
                Ab[i] -= factor * Ab[k]

        steps.append({
            'step': f'Eliminación en columna {k+1}',
            'Ab': Ab.tolist()
        })

    x = Ab[:, -1]
    steps.append({
        'step': 'Solución final',
        'x': x.tolist()
    })

    return x, steps

def format_steps(steps):
    formatted = []
    for step in steps:
        if 'Ab' in step:
            formatted.append(f"{step['step']}:\nAb = {np.array2string(np.array(step['Ab']), precision=4)}")
        elif 'x' in step:
            formatted.append(f"{step['step']}:\nx = {np.array2string(np.array(step['x']), precision=4)}")
    return formatted

def plot_solution(A, b, x):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(x) + 1), x, 'bo-', label='Solución')
    plt.title('Solución del sistema de ecuaciones')
    plt.xlabel('Variable')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    plt.savefig('static/gauss_jordan_solution.png')
    plt.close()