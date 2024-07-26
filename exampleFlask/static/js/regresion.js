document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('regresionForm');
    const tipoRegresion = document.getElementById('tipoRegresion');
    const gradoInput = document.getElementById('gradoInput');

    tipoRegresion.addEventListener('change', function() {
        if (this.value === 'Polinomial') {
            gradoInput.style.display = 'block';
        } else {
            gradoInput.style.display = 'none';
        }
    });

    form.addEventListener('submit', handleSubmit);

    function handleSubmit(event) {
        event.preventDefault();
        const xValues = form['xValues'].value.split(',').map(Number);
        const yValues = form['yValues'].value.split(',').map(Number);
        const tipoRegresion = form['tipoRegresion'].value;
        const grado = tipoRegresion === 'Polinomial' ? parseInt(form['grado'].value) : 1;

        fetch('/api/regresion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ xValues, yValues, tipoRegresion, grado })
        })
        .then(response => response.json())
        .then(result => {
            document.getElementById('ecuacion').textContent = result.ecuacion;
            document.getElementById('rSquared').textContent = result.r_squared.toFixed(4);
            document.getElementById('grafica').src = '/static/regresion_plot.png?' + new Date().getTime();
            document.getElementById('resultados').style.display = 'block';
        })
        .catch(error => console.error('Error:', error));
    }
});