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

import os

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

if __name__ == '__main__':
    app.run(debug=True)

