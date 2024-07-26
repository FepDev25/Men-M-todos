from flask import Flask, request, render_template, jsonify, send_from_directory
from biseccion import *   
from falsa_pocision import *  
from secante import *
from newton_raphson import newton_raphson
from Euler import *
from EulerMejorado import euler_mejorado 
from RungeKuta import *
from trazadores_cuadraticos import *
from trazadores_cubicos import *
from simpson13 import *
from simpson38 import *
from trapecio import *
from derivada_extrapol_r import *
from gauss_simple import gauss_simple, format_steps
from gauss_simple_pivoteo import resolver_gauss_simple_pivoteo
from gauss_jordan import gauss_jordan, format_steps, plot_solution
from cuadratura_gauss import cuadratura_gauss
from regresion import calcular_regresion
from interpolacion import *
from diferenciacion_numerica import *
from derivadas_irregulares import *

import os
import numpy as np 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biseccion.html')
def biseccion_page():
    return render_template('biseccion.html')

@app.route('/falsa_pocision.html')
def falsa_posicion_page():
    return render_template('falsa_pocision.html')

@app.route('/trazadores_cuadraticos.html')
def trazadores_cuadraticos_page():
    return render_template('trazadores_cuadraticos.html')
@app.route('/trazadores_cubicos.html')
def trazadores_cubicos_page():
    return render_template('trazadores_cubicos.html')

@app.route('/diferenciacion_numerica.html')
def diferenciacion_numerica_page():
    return render_template('diferenciacion_numerica.html')

@app.route('/derivadas_irregulares.html')
def derivadas_irregulares_page():
    return render_template('derivadas_irregulares.html')


@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/secante.html')
def secante_page():
    return render_template('secante.html')

@app.route('/newton.html')
def newton_page():
    return render_template('newton.html')

@app.route('/euler.html')
def euler_page():
    return render_template('euler.html')

@app.route('/euler_mejorado.html')
def euler_mejorado_page():
    return render_template('euler_mejorado.html')

@app.route('/runge_kutta.html')
def runge_kutta_page():
    return render_template('runge_kutta.html')

@app.route('/simpson1-3.html')
def simpson13_page():
    return render_template('simpson1-3.html')

@app.route('/simpson3-8.html')
def simpson38_page():
    return render_template('simpson3-8.html')

@app.route('/trapecio.html')
def trapecio_page():
    return render_template('trapecio.html')

@app.route('/extrapolacion_richardson.html')
def extrapolacion_richardson_page():
    return render_template('extrapolacion_richardson.html')

@app.route('/gauss_simple.html')
def gauss_simple_page():
    return render_template('gauss_simple.html')

@app.route('/gauss_simple_pivoteo.html')
def gauss_simple_pivoteo_page():
    return render_template('gauss_simple_pivoteo.html')

@app.route('/gauss_jordan.html')
def gauss_jordan_page():
    return render_template('gauss_jordan.html')

@app.route('/cuadratura_gauss.html')
def cuadratura_gauss_page():
    return render_template('cuadratura_gauss.html')


@app.route('/regresion.html')
def regresion_page():
    return render_template('regresion.html')



@app.route('/interpolacion.html')
def interpolacion_page():
    return render_template('interpolacion.html')

@app.route('/api/biseccion', methods=['POST'])
def api_biseccion():
    data = request.json
    xi = data.get('xi')
    xu = data.get('xu')
    funcion = data.get('funcion')
    max_pasadas = data.get('maxPasadas')
    porcentaje_aprox = data.get('porcentajeAprox')
    porcentaje_verdadero = data.get('porcentajeVerdadero')

    mensaje, raiz, pasadas, datos_iteraciones, archivo_grafica = biseccion(
        xi, xu, funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero
    )
    
    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica)

    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}'
    })

@app.route('/api/falsa_pocision', methods=['POST'])
def api_falsa_pocision():
    data = request.json
    xi = data['xi']
    xu = data['xu']
    funcion = data['funcion']
    maxPasadas = data['maxPasadas']
    porcentajeAprox = data['porcentajeAprox']
    porcentajeVerdadero = data['porcentajeVerdadero']

    mensaje, raiz, pasadas, datos_iteraciones, grafica = falsa_pocision(
        xi, xu, funcion, maxPasadas, porcentajeAprox, porcentajeVerdadero
    )  
    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
        'grafica': grafica
    })



@app.route('/api/trazadores_cuadraticos', methods=['POST'])
def api_trazadores_cuadraticos():
    datos = request.json
    x_data = datos['x_data']
    y_data = datos['y_data']
    mensaje, splines, grafica = calcular_trazadores_cuadraticos(x_data, y_data)
    return jsonify({
        'mensaje': mensaje,
        'splines': splines,
        'grafica': grafica
    })
@app.route('/api/secante', methods=['POST'])
def api_secante():
    data = request.json
    x0 = data.get('x0')
    x1 = data.get('x1')
    funcion = data.get('funcion')
    max_iteraciones = data.get('maxIteraciones')
    error_aprox = data.get('errorAprox')
    error_verdadero = data.get('errorVerdadero')

    mensaje, raiz, iteraciones, datos_iteraciones, archivo_grafica = secante(
        funcion, x0, x1, max_iteraciones, error_aprox, error_verdadero
    )
    
    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica)

    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'iteraciones': iteraciones,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}'
    })

@app.route('/api/newton_raphson', methods=['POST'])
def api_newton_raphson():
    data = request.json
    x_inicial = data.get('xInicial')
    funcion = data.get('funcion')
    limite_iteraciones = data.get('limiteIteraciones')
    valor_error_aproximado = data.get('valorErrorAproximado')
    valor_error_verdadero = data.get('valorErrorVerdadero')

    mensaje, raiz, pasadas, datos_iteraciones, archivo_grafica = newton_raphson(
        funcion, limite_iteraciones, x_inicial, valor_error_aproximado, valor_error_verdadero
    )
    
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/euler', methods=['POST'])
def api_euler():
    data = request.json
    ecuacion = data.get('ecuacion')
    x0 = data.get('x0')
    y0 = data.get('y0')
    incog = data.get('incog')
    h = data.get('h')

    mensaje, datos_iteraciones, archivo_grafica = eulerMetodo(
        ecuacion, x0, y0, incog, h
    )

    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/euler_mejorado', methods=['POST'])
def api_euler_mejorado():
    data = request.json
    ecuacion = data.get('ecuacion')
    x0 = data.get('x0')
    y0 = data.get('y0')
    incog = data.get('incog')
    h = data.get('h')

    mensaje, datos_iteraciones, archivo_grafica = euler_mejorado(
        ecuacion, x0, y0, incog, h
    )

    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/runge-kutta', methods=['POST'])
def api_runge_kutta():
    data = request.json
    ecuacion = data.get('ecuacion')
    x0 = data.get('x0')
    y0 = data.get('y0')
    incog = data.get('incog')
    h = data.get('h')

    mensaje, datos_iteraciones, archivo_grafica = rungeKuta(
        ecuacion, x0, y0, incog, h
    )

    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })
@app.route('/api/trazadores_cubicos', methods=['POST'])
def trazadores_cubicos():
    data = request.json
    x_data = data.get('x_data')
    y_data = data.get('y_data')

    if x_data is None or y_data is None:
        return jsonify({'error': 'Datos de entrada faltantes'}), 400

    try:
        mensaje, splines, grafica = calcular_trazadores_cubicos(x_data, y_data)
        return jsonify({'mensaje': mensaje, 'splines': splines, 'grafica': grafica})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/simpson1-3', methods=['POST'])
def api_simpson_tercio():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    n = data.get('n')
    funcion = data.get('funcion')

    mensaje, area, archivo_grafica, integral_analitica, error = simpson_tercio(funcion, a, b, n)
    
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'area': area,
        'integral_analitica': integral_analitica,
        'error': error,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/simpson3-8', methods=['POST'])
def api_simpson_octavo():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    n = data.get('n')
    funcion = data.get('funcion')

    mensaje, area, archivo_grafica, integral_analitica, error = simpson_tres_octavos(funcion, a, b, n)
    
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'area': area,
        'integral_analitica': integral_analitica,
        'error': error,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/trapecio', methods=['POST'])
def api_trapecio():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    n = data.get('n')
    funcion = data.get('funcion')

    mensaje, area, archivo_grafica, integral_analitica, error = metodo_trapecio(funcion, a, b, n)
    
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'area': area,
        'integral_analitica': integral_analitica,
        'error': error,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/extrapolacion_richardson', methods=['POST'])
def api_extrapolacion_richardson():
    data = request.json
    x0 = data.get('x0')
    h1 = data.get('h1')
    h2 = data.get('h2')
    funcion = data.get('funcion')

    mensaje, derivada, derivada_analitica, error, archivo_grafica = extrapolacion_richardson(
        funcion, x0, h1, h2
    )
    
    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica)

    return jsonify({
        'mensaje': mensaje,
        'derivada': derivada,
        'derivada_analitica': derivada_analitica,
        'error': error,
        'grafica': f'/static/{archivo_grafica_nombre}'
    })

@app.route('/api/interpolacion', methods=['POST'])
def api_interpolacion():
    data = request.json
    x = np.array(data['x'])
    y = np.array(data['y'])
    nuevos_x = np.array(data['nuevos_x'])
    metodo = data['metodo']
    grado = data.get('grado', 3)  # Grado por defecto para Splines B-Spline

    if metodo == 'lineal':
        x, y, nuevos_x, nuevos_y, grafica = interpolacion_lineal(x, y, nuevos_x)
    elif metodo == 'splines_cubicos':
        x, y, nuevos_x, nuevos_y, grafica = interpolacion_splines_cubicos(x, y, nuevos_x)
    elif metodo == 'splines_bspline':
        x, y, nuevos_x, nuevos_y, grafica = interpolacion_splines_bspline(x, y, nuevos_x, grado)
    elif metodo == 'polinomios_lagrange':
        x, y, nuevos_x, nuevos_y, grafica = interpolacion_polinomios_lagrange(x, y, nuevos_x)
    else:
        return jsonify({'mensaje': 'Método de interpolación no reconocido'}), 400

    return jsonify({
        'x': x.tolist(),
        'y': y.tolist(),
        'nuevos_x': nuevos_x.tolist(),
        'datos_interpolacion': nuevos_y.tolist(),
        'grafica': grafica
    })
@app.route('/api/diferenciacion_numerica', methods=['POST'])
def api_diferenciacion_numerica():
    datos = request.json
    funcion = datos.get('funcion')
    intervalo = datos.get('intervalo')
    tamaño_paso = datos.get('tamaño_paso')
    metodo = datos.get('metodo')

    try:
        mensaje, resultado = calcular_diferenciacion_numerica(funcion, intervalo, tamaño_paso, metodo)
        return jsonify({'mensaje': mensaje, 'resultado': resultado})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/derivadas_irregulares', methods=['POST'])
def api_derivadas_irregulares():
    data = request.json
    pares = data.get('pares', [])
    punto_estimar = data.get('punto_estimar')
    metodo = data.get('metodo')
    
    if not pares or punto_estimar is None or not metodo:
        return jsonify({'error': 'Datos incompletos.'}), 400
    
    try:
        mensaje, resultado, grafica_path = calcular_derivadas_irregulares(pares, punto_estimar, metodo)
        return jsonify({'mensaje': mensaje, 'resultado': resultado, 'grafica': grafica_path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)


#gauss simple
@app.route('/api/gauss_simple', methods=['POST'])
def api_gauss_simple():
    data = request.json
    A = np.array(data['A'])
    b = np.array(data['b'])

    try:
        x, steps = gauss_simple(A, b)
        formatted_steps = format_steps(steps)
        return jsonify({
            'solution': x.tolist(),
            'steps': formatted_steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/gauss_simple_pivoteo', methods=['POST'])
def api_gauss_simple_pivoteo():
    data = request.json
    A = data.get('A')
    b = data.get('b')

    try:
        solucion, pasos = resolver_gauss_simple_pivoteo(A, b)
        return jsonify({
            'solucion': solucion,
            'pasos': pasos
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/gauss_jordan', methods=['POST'])
def api_gauss_jordan():
    data = request.json
    A = np.array(data['A'])
    b = np.array(data['b'])

    try:
        x, steps = gauss_jordan(A, b)
        formatted_steps = format_steps(steps)
        plot_solution(A, b, x)
        return jsonify({
            'solution': x.tolist(),
            'steps': formatted_steps
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/cuadratura_gauss', methods=['POST'])
def api_cuadratura_gauss():
    data = request.json
    a = data.get('a')
    b = data.get('b')
    n = data.get('n')
    funcion = data.get('funcion')

    mensaje, integral, archivo_grafica, integral_analitica, error = cuadratura_gauss(funcion, a, b, n)
    
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'integral': integral,
        'integral_analitica': integral_analitica,
        'error': error,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
    })

@app.route('/api/regresion', methods=['POST'])
def api_regresion():
    data = request.json
    x = np.array(data['xValues'])
    y = np.array(data['yValues'])
    tipo_regresion = data['tipoRegresion']
    grado = data['grado']

    try:
        resultado = calcular_regresion(x, y, tipo_regresion, grado)
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)