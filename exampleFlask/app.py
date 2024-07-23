from flask import Flask, request, render_template, jsonify
from biseccion import *     

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/biseccion.html')
def biseccion_page():
    return render_template('biseccion.html')

@app.route('/api/biseccion', methods=['POST'])
def api_biseccion():
    data = request.get_json()
    
    xi = float(data.get('xi'))
    xu = float(data.get('xu'))
    funcion = data.get('funcion')
    max_pasadas = int(data.get('maxPasadas'))
    porcentaje_aprox = float(data.get('porcentajeAprox'))
    porcentaje_verdadero = float(data.get('porcentajeVerdadero'))

    mensaje, xi, pasadas, datos_iteraciones = biseccion(xi, xu, funcion, max_pasadas, porcentaje_aprox, porcentaje_verdadero)
        
    
    return jsonify({
        'mensaje': mensaje,
        'raiz': xi,
        'pasadas': pasadas,
        'datos_iteraciones': datos_iteraciones,
    })

if __name__ == '__main__':
    app.run(debug=True)

