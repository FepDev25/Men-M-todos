document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('trazadoresCuadraticosForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const xData = document.getElementById('x_data').value.trim();
        const yData = document.getElementById('y_data').value.trim();

        if (!xData || !yData) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const xDataArray = xData.split(',').map(Number);
        const yDataArray = yData.split(',').map(Number);

        if (xDataArray.length !== yDataArray.length) {
            alert('Los datos de X e Y deben tener la misma longitud.');
            return;
        }

        const data = {
            x_data: xDataArray,
            y_data: yDataArray
        };

        fetch('/api/trazadores_cuadraticos', {
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

            resultadosDiv.querySelector('#mensaje').textContent = result.mensaje;

            tablaResultados.innerHTML = '';

            result.splines.forEach(spline => {
                const row = tablaResultados.insertRow();
                row.insertCell(0).textContent = spline.a;
                row.insertCell(1).textContent = spline.b;
                row.insertCell(2).textContent = spline.c;
                row.insertCell(3).textContent = spline.x0;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
