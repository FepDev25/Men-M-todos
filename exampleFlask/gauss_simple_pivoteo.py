import numpy as np

def gauss_simple_pivoteo(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    x = np.zeros(n)
    pasos = []

    for k in range(n-1):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(A[k:, k])) + k
        if max_index != k:
            A[[k, max_index]] = A[[max_index, k]]
            b[[k, max_index]] = b[[max_index, k]]
        
        pasos.append({
            'etapa': f'Pivoteo en columna {k+1}',
            'A': A.tolist(),
            'b': b.tolist()
        })

        for i in range(k+1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] -= factor * A[k, k:]
            b[i] -= factor * b[k]

        pasos.append({
            'etapa': f'Eliminación en columna {k+1}',
            'A': A.tolist(),
            'b': b.tolist()
        })

    # Sustitución hacia atrás
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:], x[k+1:])) / A[k,k]

    pasos.append({
        'etapa': 'Solución final',
        'x': x.tolist()
    })

    return x, pasos

def formato_matriz(A, b):
    return [row + [bi] for row, bi in zip(A, b)]

def resolver_gauss_simple_pivoteo(A, b):
    A = np.array(A)
    b = np.array(b)
    x, pasos = gauss_simple_pivoteo(A, b)

    # Formatear los pasos para una mejor visualización
    pasos_formateados = []
    for paso in pasos:
        if 'A' in paso and 'b' in paso:
            matriz_aumentada = formato_matriz(paso['A'], paso['b'])
            pasos_formateados.append({
                'etapa': paso['etapa'],
                'matriz': matriz_aumentada
            })
        elif 'x' in paso:
            pasos_formateados.append({
                'etapa': paso['etapa'],
                'solucion': paso['x']
            })

    return x.tolist(), pasos_formateados