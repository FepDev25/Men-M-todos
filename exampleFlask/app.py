from flask import Flask, request, render_template, jsonify
from biseccion import *   
from falsa_pocision import *  

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
    return jsonify({
        'mensaje': mensaje,
        'raiz': raiz,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
        'grafica': archivo_grafica
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



if __name__ == '__main__':
    app.run(debug=True)

