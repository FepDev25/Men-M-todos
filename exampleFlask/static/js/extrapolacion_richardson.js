document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('richardsonForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const x0 = document.getElementById('x0').value.trim();
        const h1 = document.getElementById('h1').value.trim();
        const h2 = document.getElementById('h2').value.trim();
        const funcion = document.getElementById('funcion').value.trim();

        if (!x0 || !h1 || !h2 || !funcion) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const x0Num = parseFloat(x0);
        const h1Num = parseFloat(h1);
        const h2Num = parseFloat(h2);

        const data = {
            x0: x0Num,
            h1: h1Num,
            h2: h2Num,
            funcion: funcion
        };

        fetch('/api/extrapolacion_richardson', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const resultadosDiv = document.getElementById('resultados');

            resultadosDiv.querySelector('#mensaje').textContent = result.mensaje;
            resultadosDiv.querySelector('#derivada').textContent = result.derivada;
            resultadosDiv.querySelector('#derivadaAnalitica').textContent = result.derivada_analitica;
            resultadosDiv.querySelector('#error').textContent = result.error;

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = '/static/grafica_derivada_richardson.png?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
