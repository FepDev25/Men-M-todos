document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('gaussJordanForm');
    const matrixSizeInput = document.getElementById('matrixSize');
    const generateMatrixButton = document.getElementById('generateMatrix');
    const matrixInputs = document.getElementById('matrixInputs');

    generateMatrixButton.addEventListener('click', generateMatrixInputs);
    form.addEventListener('submit', handleSubmit);

    function generateMatrixInputs() {
        const size = parseInt(matrixSizeInput.value);
        let html = '';

        for (let i = 0; i < size; i++) {
            for (let j = 0; j < size; j++) {
                html += `<input class="controls matrix-input" type="number" name="A_${i}_${j}" placeholder="A[${i+1}][${j+1}]">`;
            }
            html += `<input class="controls matrix-input" type="number" name="b_${i}" placeholder="b[${i+1}]"><br>`;
        }

        matrixInputs.innerHTML = html;
    }

    function handleSubmit(event) {
        event.preventDefault();
        const size = parseInt(matrixSizeInput.value);
        const A = [];
        const b = [];

        for (let i = 0; i < size; i++) {
            A[i] = [];
            for (let j = 0; j < size; j++) {
                A[i][j] = parseFloat(form[`A_${i}_${j}`].value);
            }
            b[i] = parseFloat(form[`b_${i}`].value);
        }

        fetch('/api/gauss_jordan', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ A, b })
        })
        .then(response => response.json())
        .then(result => {
            document.getElementById('pasos').textContent = result.steps.join('\n\n');
            document.getElementById('solucion').textContent = `x = [${result.solution.join(', ')}]`;
            document.getElementById('grafica').src = '/static/gauss_jordan_solution.png?' + new Date().getTime();
            document.getElementById('resultados').style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    }
});