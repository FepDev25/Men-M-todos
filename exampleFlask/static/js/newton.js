document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('newtonRaphsonForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const xInicial = document.getElementById('xInicial').value.trim();
        const funcion = document.getElementById('funcion').value.trim();
        const limiteIteraciones = document.getElementById('limiteIteraciones').value.trim();
        const valorErrorAproximado = document.getElementById('valorErrorAproximado').value.trim();
        const valorErrorVerdadero = document.getElementById('valorErrorVerdadero').value.trim();

        if (!xInicial || !funcion || !limiteIteraciones || !valorErrorAproximado || !valorErrorVerdadero) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const xInicialNum = parseFloat(xInicial);
        const limiteIteracionesNum = parseInt(limiteIteraciones);
        const valorErrorAproximadoNum = parseFloat(valorErrorAproximado);
        const valorErrorVerdaderoNum = parseFloat(valorErrorVerdadero);

        const data = {
            xInicial: xInicialNum,
            funcion: funcion,
            limiteIteraciones: limiteIteracionesNum,
            valorErrorAproximado: valorErrorAproximadoNum,
            valorErrorVerdadero: valorErrorVerdaderoNum
        };

        fetch('/api/newton_raphson', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const resultadosDiv = document.getElementById('resultados');
            const tablaResultados = document.getElementById('tabla-resultados').getElementsByTagName('tbody')[0];

            resultadosDiv.querySelector('#raiz').textContent = result.raiz;
            resultadosDiv.querySelector('#mensaje').textContent = result.mensaje;
            resultadosDiv.querySelector('#iteraciones').textContent = result.pasadas;

            tablaResultados.innerHTML = '';

            result.datos_iteraciones.forEach(iteracion => {
                const row = tablaResultados.insertRow();
                row.insertCell(0).textContent = iteracion.Xi;
                row.insertCell(1).textContent = iteracion['Xi+1'];
                row.insertCell(2).textContent = iteracion.valor_verdadero;
                row.insertCell(3).textContent = iteracion.error_verdadero;
                row.insertCell(4).textContent = iteracion.error_verdadero_porcentual;
                row.insertCell(5).textContent = iteracion.error_aproximado;
                row.insertCell(6).textContent = iteracion.error_aproximado_prcentual;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
