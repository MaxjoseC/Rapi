const apiClientesURL = "http://localhost:8000/api/clientes/";
const apiPedidosURL = "http://localhost:8000/api/pedidos/";

async function loadPedidos() {
  try {
      const response = await fetch(apiPedidosURL);
      if (!response.ok) throw new Error("Error al cargar los pedidos");

      const pedidos = await response.json();
      const tableBody = document.querySelector("#pedidos-table tbody");
      tableBody.innerHTML = "";

      for (const pedido of pedidos) {
          const clienteResponse = await fetch(`${apiClientesURL}${pedido.cliente}/`);
          const cliente = await clienteResponse.json();
          
          const total = parseFloat(pedido.total);
          const totalFormatted = !isNaN(total) ? total.toFixed(2) : 'N/A';

          const row = document.createElement("tr");
          row.innerHTML = `
              <td>${pedido.id}</td>
              <td>${cliente.nombre}</td> <!-- Ahora obtenemos el nombre del cliente -->
              <td>${pedido.fecha}</td>
              <td>${pedido.estado}</td>
              <td>${totalFormatted}</td>
              <td>
                  <button onclick="editPedido(${pedido.id})">Editar</button>
                  <button onclick="deletePedido(${pedido.id})">Eliminar</button>
              </td>
          `;
          tableBody.appendChild(row);
      }
  } catch (error) {
      console.error(error);
      Swal.fire("Error", "No se pudieron cargar los pedidos.", "error");
  }
}



async function cargarClientes() {
    try {
        const response = await fetch(apiClientesURL);
        if (!response.ok) throw new Error("Error al cargar los clientes");

        const clientes = await response.json();
        const selectCliente = document.querySelector("#cliente-select");

        selectCliente.innerHTML = ''; 

        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = "Seleccionar cliente";
        selectCliente.appendChild(defaultOption);

        // Agregar clientes al select
        clientes.forEach(cliente => {
            const option = document.createElement("option");
            option.value = cliente.id;
            option.textContent = cliente.nombre;
            selectCliente.appendChild(option);
        });
    } catch (error) {
        console.error(error);
        Swal.fire("Error", "No se pudieron cargar los clientes.", "error");
    }
}

function mostrarFormularioCrearPedido() {
    Swal.fire({
        title: "Crear Pedido",
        html: `
            <form id="form-crear-pedido">
                <div>
                    <label for="cliente-select" style="display: block; margin-bottom: 5px;">Cliente</label>
                    <select id="cliente-select" required style="width: 100%; padding: 5px;"></select>
                </div>
                <div>
                    <label for="total" style="display: block; margin-bottom: 5px;">Total</label>
                    <input type="number" id="total" min="0" step="0.01" required style="width: 100%; padding: 5px;" />
                </div>
                <div>
                    <label for="estado" style="display: block; margin-bottom: 5px;">Estado</label>
                    <select id="estado" required style="width: 100%; padding: 5px;">
                        <option value="pendiente">Pendiente</option>
                        <option value="completado">Completado</option>
                        <option value="cancelado">Cancelado</option>
                    </select>
                </div>
            </form>
        `,
        confirmButtonText: "Crear",
        showCancelButton: true,
        didOpen: () => {
            cargarClientes(); 
        },
        preConfirm: () => {
            const clienteId = document.getElementById("cliente-select").value;
            const total = document.getElementById("total").value.trim();
            const estado = document.getElementById("estado").value;

            if (!clienteId || !total || !estado) {
                Swal.showValidationMessage("Todos los campos son obligatorios");
                return false;
            }

            return { clienteId, total, estado };
        },
    }).then(async (result) => {
        if (result.isConfirmed) {
            const { clienteId, total, estado } = result.value;

            const pedidoData = {
                cliente: clienteId,
                total: parseFloat(total),     
                estado,
            };

            try {
                const response = await fetch(apiPedidosURL, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify(pedidoData),
                });

                if (!response.ok) throw new Error("Error al crear el pedido");

                Swal.fire("Pedido creado", "El pedido se ha creado correctamente.", "success");
                loadPedidos();
            } catch (error) {
                Swal.fire("Error", "Hubo un problema al crear el pedido.", "error");
            }
        }
    });
}

async function editPedido(id) {
    Swal.fire({
        title: "Función en desarrollo",
        text: `Editar pedido con ID: ${id}`,
        icon: "info",
    });
}

async function deletePedido(id) {
    const confirm = await Swal.fire({
        title: "¿Estás seguro?",
        text: "No podrás recuperar este pedido una vez eliminado.",
        icon: "warning",
        showCancelButton: true,
        confirmButtonText: "Sí, eliminar",
        cancelButtonText: "Cancelar",
    });

    if (confirm.isConfirmed) {
        try {
            const response = await fetch(`${apiPedidosURL}${id}/`, { method: "DELETE" });
            if (!response.ok) throw new Error("Error al eliminar el pedido");

            Swal.fire("Eliminado", "El pedido se ha eliminado correctamente.", "success");
            loadPedidos();
        } catch (error) {
            Swal.fire("Error", "No se pudo eliminar el pedido.", "error");
        }
    }
}

document.addEventListener("DOMContentLoaded", () => {
    loadPedidos();

    const btnCrearPedido = document.getElementById("btn-crear-pedido");
    if (btnCrearPedido) {
        btnCrearPedido.addEventListener("click", mostrarFormularioCrearPedido);
    }
});
