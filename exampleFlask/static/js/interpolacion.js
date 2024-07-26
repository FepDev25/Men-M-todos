document.addEventListener('DOMContentLoaded', function() {
    const metodoSelect = document.getElementById('metodo');
    const gradoContainer = document.getElementById('grado-container');

    metodoSelect.addEventListener('change', function() {
        if (this.value === 'splines_bspline') {
            gradoContainer.style.display = 'block';
        } else {
            gradoContainer.style.display = 'none';
        }
    });

    document.getElementById('interpolacionForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const x = document.getElementById('x').value.trim().split(',').map(Number);
        const y = document.getElementById('y').value.trim().split(',').map(Number);
        const nuevosX = document.getElementById('nuevos_x').value.trim().split(',').map(Number);
        const metodo = document.getElementById('metodo').value;
        let grado = null;

        if (metodo === 'splines_bspline') {
            grado = parseInt(document.getElementById('grado').value.trim());
        }

        if (x.length === 0 || y.length === 0 || nuevosX.length === 0 || (metodo === 'splines_bspline' && isNaN(grado))) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        if (metodo === 'splines_bspline' && (grado >= nuevosX.length) || (grado > 5)) {
            alert('El grado debe ser menor que el número de nuevos datos a buscar y maximo 5.');
            return;
        }

        const data = {
            x: x,
            y: y,
            nuevos_x: nuevosX,
            metodo: metodo,
            grado: grado
        };

        fetch('/api/interpolacion', {
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

            resultadosDiv.querySelector('#x').textContent = result.x;
            resultadosDiv.querySelector('#y').textContent = result.y;

            tablaResultados.innerHTML = '';

            result.datos_interpolacion.forEach((dato, index) => {
                const row = tablaResultados.insertRow();
                row.insertCell(0).textContent = result.nuevos_x[index];
                row.insertCell(1).textContent = dato;
            });

            const graficaImg = document.getElementById('grafica');
            graficaImg.src = '/static/grafica_interpolacion.png?t=' + new Date().getTime();
            graficaImg.style.display = 'block'; 
        })
        .catch(error => console.error('Error:', error));
    });
});
