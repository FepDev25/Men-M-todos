document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('gaussSimplePivoteoForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const matrizA = document.getElementById('matrizA').value.split(';').map(row => row.split(',').map(Number));
        const vectorB = document.getElementById('vectorB').value.split(',').map(Number);

        fetch('/api/gauss_simple_pivoteo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                A: matrizA,
                b: vectorB
            })
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                alert(result.error);
                return;
            }

            document.getElementById('solucion').textContent = JSON.stringify(result.solucion, null, 2);

            const pasosDiv = document.getElementById('pasos');
            pasosDiv.innerHTML = '';

            result.pasos.forEach((paso, index) => {
                const pasoDiv = document.createElement('div');
                pasoDiv.innerHTML = `<h5>Paso ${index + 1}: ${paso.etapa}</h5>`;

                if (paso.matriz) {
                    const tabla = crearTablaMatriz(paso.matriz);
                    pasoDiv.appendChild(tabla);
                } else if (paso.solucion) {
                    const pre = document.createElement('pre');
                    pre.textContent = JSON.stringify(paso.solucion, null, 2);
                    pasoDiv.appendChild(pre);
                }

                pasosDiv.appendChild(pasoDiv);
            });
        })
        .catch(error => console.error('Error:', error));
    });
});

function crearTablaMatriz(matriz) {
    const tabla = document.createElement('table');
    tabla.style.borderCollapse = 'collapse';

    matriz.forEach(fila => {
        const tr = document.createElement('tr');
        fila.forEach(valor => {
            const td = document.createElement('td');
            td.textContent = valor.toFixed(4);
            td.style.border = '1px solid black';
            td.style.padding = '5px';
            tr.appendChild(td);
        });
        tabla.appendChild(tr);
    });

    return tabla;
}