document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('gaussJordanForm');
    const matrixSizeInput = document.getElementById('matrixSize');
    const matrixInputsContainer = document.getElementById('matrixInputs');
    const generateMatrixButton = document.getElementById('generateMatrix');

    generateMatrixButton.addEventListener('click', function() {
        const size = parseInt(matrixSizeInput.value);
        matrixInputsContainer.innerHTML = '';

        for (let i = 0; i < size; i++) {
            for (let j = 0; j < size + 1; j++) {
                const input = document.createElement('input');
                input.type = 'number';
                input.className = 'controls';
                input.id = `matrix_${i}_${j}`;
                input.name = `matrix_${i}_${j}`;
                input.placeholder = `A[${i + 1}][${j + 1}]`;
                matrixInputsContainer.appendChild(input);
            }
            matrixInputsContainer.appendChild(document.createElement('br'));
        }
    });

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const size = parseInt(matrixSizeInput.value);
        const matrix = [];

        for (let i = 0; i < size; i++) {
            const row = [];
            for (let j = 0; j < size + 1; j++) {
                const input = document.getElementById(`matrix_${i}_${j}`).value.trim();
                if (!input) {
                    alert('Por favor, complete todos los campos de la matriz.');
                    return;
                }
                row.push(parseFloat(input));
            }
            matrix.push(row);
        }

        const data = {
            matrix: matrix
        };

        fetch('/api/gauss_jordan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const pasos = document.getElementById('pasos');
            const solucion = document.getElementById('solucion');

            pasos.textContent = result.pasos.join('\n');
            solucion.textContent = result.solucion.join('\n');
        })
        .catch(error => console.error('Error:', error));
    });
});
