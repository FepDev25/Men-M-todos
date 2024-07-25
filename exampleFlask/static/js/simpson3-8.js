document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('simpsonForm38').addEventListener('submit', function(event) {
        event.preventDefault();

        const a = document.getElementById('a').value.trim();
        const b = document.getElementById('b').value.trim();
        const n = document.getElementById('n').value.trim();
        const funcion = document.getElementById('funcion').value.trim();

        if (!a || !b || !n || !funcion) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const aNum = parseFloat(a);
        const bNum = parseFloat(b);
        const nNum = parseInt(n);

        const data = {
            a: aNum,
            b: bNum,
            n: nNum,
            funcion: funcion
        };

        fetch('/api/simpson3-8', {
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
            resultadosDiv.querySelector('#area').textContent = result.area;
            resultadosDiv.querySelector('#integral_analitica').textContent = result.integral_analitica;
            resultadosDiv.querySelector('#error').textContent = result.error;

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
