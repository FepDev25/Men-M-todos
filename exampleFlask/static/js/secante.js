document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('secanteForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const x0 = document.getElementById('x0').value.trim();
        const x1 = document.getElementById('x1').value.trim();
        const funcion = document.getElementById('funcion').value.trim();
        const maxIteraciones = document.getElementById('maxIteraciones').value.trim();
        const errorAprox = document.getElementById('errorAprox').value.trim();
        const errorVerdadero = document.getElementById('errorVerdadero').value.trim();

        if (!x0 || !x1 || !funcion || !maxIteraciones || !errorAprox || !errorVerdadero) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const x0Num = parseFloat(x0);
        const x1Num = parseFloat(x1);
        const maxIteracionesNum = parseInt(maxIteraciones);
        const errorAproxNum = parseFloat(errorAprox);
        const errorVerdaderoNum = parseFloat(errorVerdadero);

        const data = {
            x0: x0Num,
            x1: x1Num,
            funcion: funcion,
            maxIteraciones: maxIteracionesNum,
            errorAprox: errorAproxNum,
            errorVerdadero: errorVerdaderoNum
        };

        fetch('/api/secante', {
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
            resultadosDiv.querySelector('#iteraciones').textContent = result.iteraciones;

            tablaResultados.innerHTML = '';

            result.datos_iteraciones.forEach(iteracion => {
                const row = tablaResultados.insertRow();
                row.insertCell(0).textContent = iteracion.x0;
                row.insertCell(1).textContent = iteracion.fx0;
                row.insertCell(2).textContent = iteracion.x1;
                row.insertCell(3).textContent = iteracion.fx1;
                row.insertCell(4).textContent = iteracion.xi;
                row.insertCell(5).textContent = iteracion.valor_verdadero;
                row.insertCell(6).textContent = iteracion.error_verdadero;
                row.insertCell(7).textContent = iteracion.error_verdadero_porcentual;
                row.insertCell(8).textContent = iteracion.error_aprox;
                row.insertCell(9).textContent = iteracion.error_aprox_porcentual;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
