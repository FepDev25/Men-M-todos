document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('falsaposForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const xi = document.getElementById('xi').value.trim();
        const xu = document.getElementById('xu').value.trim();
        const funcion = document.getElementById('funcion').value.trim();
        const maxPasadas = document.getElementById('maxPasadas').value.trim();
        const porcentajeAprox = document.getElementById('porcentajeAprox').value.trim();
        const porcentajeVerdadero = document.getElementById('porcentajeVerdadero').value.trim();

        if (!xi || !xu || !funcion || !maxPasadas || !porcentajeAprox || !porcentajeVerdadero) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const xiNum = parseFloat(xi);
        const xuNum = parseFloat(xu);
        const maxPasadasNum = parseInt(maxPasadas);
        const porcentajeAproxNum = parseFloat(porcentajeAprox);
        const porcentajeVerdaderoNum = parseFloat(porcentajeVerdadero);

        const data = {
            xi: xiNum,
            xu: xuNum,
            funcion: funcion,
            maxPasadas: maxPasadasNum,
            porcentajeAprox: porcentajeAproxNum,
            porcentajeVerdadero: porcentajeVerdaderoNum
        };

        fetch('/api/falsa_pocision', {
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
                row.insertCell(0).textContent = iteracion.xi;
                row.insertCell(1).textContent = iteracion.fxi;
                row.insertCell(2).textContent = iteracion.xu;
                row.insertCell(3).textContent = iteracion.fxu;
                row.insertCell(4).textContent = iteracion.xr;
                row.insertCell(5).textContent = iteracion.fxr;
                row.insertCell(6).textContent = iteracion.valor_verdadero;
                row.insertCell(7).textContent = iteracion.error_verdadero;
                row.insertCell(8).textContent = iteracion.error_verdadero_porcentual;
                row.insertCell(9).textContent = iteracion.error_aprox;
                row.insertCell(10).textContent = iteracion.error_porcentual;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = '/static/static/grafica.png?t=' + new Date().getTime();
            graficaImg.style.display = 'block'; 
        })
        .catch(error => console.error('Error:', error));
    });
});
