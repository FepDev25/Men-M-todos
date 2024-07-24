document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('eulerMejoradoForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const ecuacion = document.getElementById('ecuacion').value.trim();
        const x0 = document.getElementById('x0').value.trim();
        const y0 = document.getElementById('y0').value.trim();
        const incog = document.getElementById('incog').value.trim();
        const h = document.getElementById('h').value.trim();

        if (!ecuacion || !x0 || !y0 || !incog || !h) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const x0Num = parseFloat(x0);
        const y0Num = parseFloat(y0);
        const incogNum = parseFloat(incog);
        const hNum = parseFloat(h);

        const data = {
            ecuacion: ecuacion,
            x0: x0Num,
            y0: y0Num,
            incog: incogNum,
            h: hNum
        };

        fetch('/api/euler_mejorado', {
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

            result.datos_iteraciones.forEach(iteracion => {
                const row = tablaResultados.insertRow();
                row.insertCell(0).textContent = iteracion.xi;
                row.insertCell(1).textContent = iteracion.yi;
                row.insertCell(2).textContent = iteracion.Yn_1_elv;
                row.insertCell(3).textContent = iteracion.Xn_1;
                row.insertCell(4).textContent = iteracion['Yi+1'];
                row.insertCell(5).textContent = iteracion.y_analitica;
                row.insertCell(6).textContent = iteracion.error;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = result.grafica + '?t=' + new Date().getTime();
            graficaImg.style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    });
});
