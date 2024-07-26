document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('derivadasIrregularesForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const pares = document.getElementById('pares').value.trim();
        const puntoEstimar = parseFloat(document.getElementById('punto_estimar').value.trim());
        const metodo = document.getElementById('metodo').value;

        if (!pares || isNaN(puntoEstimar)) {
            alert('Por favor, complete todos los campos correctamente.');
            return;
        }

        const paresArray = pares.split(';').map(pair => {
            const [x, y] = pair.split(',').map(Number);
            return [x, y];
        });

        const data = {
            pares: paresArray,
            punto_estimar: puntoEstimar,
            metodo: metodo
        };

        fetch('/api/derivadas_irregulares', {
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
            if (result.grafica && result.grafica !== 'No aplica para este método.') {
                graficaImg.src = '/static/' + result.grafica + '?t=' + new Date().getTime();
                graficaImg.style.display = 'block';
            } else {
                graficaImg.style.display = 'none';
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
