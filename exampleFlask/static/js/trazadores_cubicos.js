document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("trazadoresCubicosForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const data = {
            xi: parseFloat(document.getElementById("xi").value),
            xu: parseFloat(document.getElementById("xu").value),
            funcion: document.getElementById("funcion").value
        };

        fetch("/api/trazadores_cubicos", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(result => {
            document.getElementById("mensaje").textContent = result.mensaje;

            const tbody = document.getElementById("tabla-resultados").getElementsByTagName("tbody")[0];
            tbody.innerHTML = "";  // Limpiar la tabla antes de agregar nuevos datos

            result.datos_iteraciones.forEach(iteracion => {
                const row = tbody.insertRow();
                row.insertCell(0).textContent = iteracion.xi;
                row.insertCell(1).textContent = iteracion.fxi;
                row.insertCell(2).textContent = iteracion.xu;
                row.insertCell(3).textContent = iteracion.fxu;
            });

            document.getElementById("grafica").src = result.grafica;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
