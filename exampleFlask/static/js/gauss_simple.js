document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('gaussSimpleForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        const size = parseInt(document.getElementById('matrixSize').value);
        const A = [];
        const b = [];

        for (let i = 0; i < size; i++) {
            const row = [];
            for (let j = 0; j < size; j++) {
                row.push(parseFloat(document.getElementById(`a${i}${j}`).value));
            }
            A.push(row);
            b.push(parseFloat(document.getElementById(`b${i}`).value));
        }

        fetch('/api/gauss_simple', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ A: A, b: b })
        })
        .then(response => response.json())
        .then(result => {
            const stepsDiv = document.getElementById('steps');
            const solutionDiv = document.getElementById('solution');

            stepsDiv.textContent = result.steps.join('\n\n');
            solutionDiv.textContent = result.solution.map((x, i) => `x${i+1} = ${x.toFixed(4)}`).join(', ');
        })
        .catch(error => console.error('Error:', error));
    });
});

function generateMatrixInputs() {
    const size = parseInt(document.getElementById('matrixSize').value);
    const matrixInputs = document.getElementById('matrixInputs');
    matrixInputs.innerHTML = '';

    for (let i = 0; i < size; i++) {
        for (let j = 0; j < size; j++) {
            const input = document.createElement('input');
            input.type = 'number';
            input.id = `a${i}${j}`;
            input.className = 'controls';
            input.placeholder = `A[${i+1}][${j+1}]`;
            matrixInputs.appendChild(input);
        }
        const bInput = document.createElement('input');
        bInput.type = 'number';
        bInput.id = `b${i}`;
        bInput.className = 'controls';
        bInput.placeholder = `b[${i+1}]`;
        matrixInputs.appendChild(bInput);
        matrixInputs.appendChild(document.createElement('br'));
    }
}