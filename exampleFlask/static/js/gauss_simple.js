document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('gaussSimpleForm').addEventListener('submit', function(event) {
        event.preventDefault();

        const matrixSize = parseInt(document.getElementById('matrixSize').value);
        const A = [];
        const b = [];

        for (let i = 0; i < matrixSize; i++) {
            A[i] = [];
            for (let j = 0; j < matrixSize; j++) {
                A[i][j] = parseFloat(document.getElementById(`A_${i}_${j}`).value);
            }
            b[i] = parseFloat(document.getElementById(`b_${i}`).value);
        }

        const data = {
            A: A,
            b: b
        };

        fetch('/api/gauss_simple', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            const steps = result.steps.join('\n\n');
            document.getElementById('steps').textContent = steps;
            document.getElementById('solution').textContent = result.solution;
        })
        .catch(error => console.error('Error:', error));
    });
});

function generateMatrixInputs() {
    const matrixSize = parseInt(document.getElementById('matrixSize').value);
    const matrixInputsDiv = document.getElementById('matrixInputs');
    matrixInputsDiv.innerHTML = '';

    for (let i = 0; i < matrixSize; i++) {
        for (let j = 0; j < matrixSize; j++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.className = 'controls';
            input.id = `A_${i}_${j}`;
            input.name = `A_${i}_${j}`;
            input.placeholder = `A[${i}][${j}]`;
            matrixInputsDiv.appendChild(input);
        }
        const inputB = document.createElement('input');
        inputB.type = 'number';
        inputB.className = 'controls';
        inputB.id = `b_${i}`;
        inputB.name = `b_${i}`;
        inputB.placeholder = `b[${i}]`;
        matrixInputsDiv.appendChild(inputB);
        matrixInputsDiv.appendChild(document.createElement('br'));
    }
}
