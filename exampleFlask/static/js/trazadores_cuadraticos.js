document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById('trazadoresForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const xi = document.getElementById('xi').value;
        const xu = document.getElementById('xu').value;
        const funcion = document.getElementById('funcion').value;
        const maxPasadas = document.getElementById('maxPasadas').value;
        const porcentajeAprox = document.getElementById('porcentajeAprox').value;
        const porcentajeVerdadero = document.getElementById('porcentajeVerdadero').value;

        const response = await fetch('/trazadores_cuadraticos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                xi: parseFloat(xi),
                xu: parseFloat(xu),
                funcion: funcion,
                max_pasadas: parseInt(maxPasadas),
                porcentaje_aprox: parseFloat(porcentajeAprox),
                porcentaje_verdadero: parseFloat(porcentajeVerdadero),
            }),
        });

        const result = await response.json();
        
        document.getElementById('mensaje').innerText = result.mensaje;
        document.getElementById('raiz').innerText = result.xr;
        document.getElementById('iteraciones').innerText = result.pasadas;

        const tablaResultados = document.getElementById('tabla-resultados').getElementsByTagName('tbody')[0];
        tablaResultados.innerHTML = '';
        
        result.datos_iteraciones.forEach(iteracion => {
            const row = tablaResultados.insertRow();
            Object.values(iteracion).forEach(val => {
                const cell = row.insertCell();
                cell.innerText = val;
            });
        });

        document.getElementById('grafica').src = result.grafica;
    });
});
