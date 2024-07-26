document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('diferenciacionNumericaForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const funcion = document.getElementById('funcion').value.trim();
        const intervalo = document.getElementById('intervalo').value.trim();
        const tamañoPaso = document.getElementById('tamaño_paso').value.trim();
        const metodo = document.getElementById('metodo').value;

        if (!funcion || !intervalo || !tamañoPaso) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const data = {
            funcion: funcion,
            intervalo: intervalo,
            tamaño_paso: tamañoPaso,
            metodo: metodo
        };

        fetch('/api/diferenciacion_numerica', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const resultadosDiv = document.getElementById('resultados');

            if (result.error) {
                alert('Error: ' + result.error);
                return;
            }

            resultadosDiv.querySelector('#mensaje').textContent = result.mensaje;

            const graficaImg = document.getElementById('grafica');
            if (result.resultado.grafica && result.resultado.grafica !== 'No aplica para este método.') {
                graficaImg.src = '/static/' + result.resultado.grafica + '?t=' + new Date().getTime();
                graficaImg.style.display = 'block';
            } else {
                graficaImg.style.display = 'none';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
