document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("diferenciacionAltaPrecisionForm");

    form.addEventListener("submit", function (event) {
        event.preventDefault();

        const data = {
            x0: parseFloat(document.getElementById("x0").value),
            h: parseFloat(document.getElementById("h").value),
            funcion: document.getElementById("funcion").value
        };

        fetch("/api/diferenciacion_alta_precision", {
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
                row.insertCell(0).textContent = iteracion.x0;
                row.insertCell(1).textContent = iteracion.h;
                row.insertCell(2).textContent = iteracion.derivada_aproximada;
                row.insertCell(3).textContent = iteracion.derivada_real;
                row.insertCell(4).textContent = iteracion.error;
                row.insertCell(5).textContent = iteracion.error_porcentual;
            });

            document.getElementById("grafica").src = result.grafica;
        })
        .catch(error => {
            console.error("Error:", error);
        });
    });
});
