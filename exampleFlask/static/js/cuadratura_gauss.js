document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('cuadraturaGaussForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const funcion = document.getElementById('funcion').value;
        const a = parseFloat(document.getElementById('a').value);
        const b = parseFloat(document.getElementById('b').value);
        const n = parseInt(document.getElementById('n').value);

        fetch('/api/cuadratura_gauss', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                funcion: funcion,
                a: a,
                b: b,
                n: n
            })
        })
        .then(response => response.json())
        .then(result => {
            document.getElementById('mensaje').textContent = result.mensaje;
            document.getElementById('integral').textContent = result.integral.toFixed(6);
            document.getElementById('integral_analitica').textContent = result.integral_analitica.toFixed(6);
            document.getElementById('error').textContent = result.error.toFixed(6);

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});