document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("derivadasIrregularForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const x_values = document.getElementById("x_values").value.split(",").map(Number);
        const y_values = document.getElementById("y_values").value.split(",").map(Number);

        const data = {
            x_values: x_values,
            y_values: y_values
        };

        fetch("/api/derivadas_irregular", {
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
                row.insertCell(0).textContent = iteracion.x;
                row.insertCell(1).textContent = iteracion.y;
                row.insertCell(2).textContent = iteracion.derivada;
            });

            document.getElementById("grafica").src = result.grafica;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
