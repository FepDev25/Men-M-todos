document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('gaussSimplePivoteoForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const matrizA = document.getElementById('matrizA').value.trim();
        const vectorB = document.getElementById('vectorB').value.trim();

        if (!matrizA || !vectorB) {
            alert('Por favor, complete todos los campos.');
            return;
        }

        const data = {
            matrizA: matrizA,
            vectorB: vectorB
        };

        fetch('/api/gauss_simple_pivoteo', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const solucionDiv = document.getElementById('solucion');
            const pasosDiv = document.getElementById('pasos');

            solucionDiv.textContent = result.solucion;

            pasosDiv.innerHTML = '';
            result.pasos.forEach(paso => {
                const pasoDiv = document.createElement('div');
                pasoDiv.classList.add('paso');
                pasoDiv.innerHTML = `<strong>${paso.etapa}:</strong><br><pre>${JSON.stringify(paso.matriz || paso.solucion, null, 2)}</pre>`;
                pasosDiv.appendChild(pasoDiv);
            });
        })
        .catch(error => console.error('Error:', error));
    });
});
