from flask import Flask, request, render_template, jsonify, send_from_directory
from biseccion import *   
from falsa_pocision import *  
from secante import *
from newton_raphson import newton_raphson
from trazadores_cuadraticos import trazadores_cuadraticos
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

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/secante.html')
def secante_page():
    return render_template('secante.html')

@app.route('/newton.html')
def newton_page():
    return render_template('newton.html')

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
    data = request.json
    xi = data.get('xi')
    xu = data.get('xu')
    funcion = data.get('funcion')
    max_pasadas = data.get('maxPasadas')
    porcentaje_aprox = data.get('porcentajeAprox')
    porcentaje_verdadero = data.get('porcentajeVerdadero')

    mensaje, raiz, pasadas, datos_iteraciones, archivo_grafica = trazadores_cuadraticos(
        xi, xu, funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero
    )
    
    # Obtener solo el nombre del archivo y no la ruta completa
    archivo_grafica_nombre = os.path.basename(archivo_grafica) if archivo_grafica else None

    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
        'grafica': f'/static/{archivo_grafica_nombre}' if archivo_grafica_nombre else ''
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


if __name__ == '__main__':
    app.run(debug=True)

