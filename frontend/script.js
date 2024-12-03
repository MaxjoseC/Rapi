const apiURL = "http://localhost:8000/api/clientes/";

// cargar clientes
async function loadClientes() {
  const response = await fetch(apiURL);
  const clientes = await response.json();
  const tableBody = document.querySelector("#clientes-table tbody");
  tableBody.innerHTML = "";
  clientes.forEach(cliente => {
    const row = document.createElement("tr");
    row.innerHTML = `
      <td>${cliente.id}</td>
      <td>${cliente.nombre}</td>
      <td>${cliente.telefono}</td>
      <td>${cliente.calle}</td>
      <td>${cliente.numero}</td>
      <td>${cliente.sector}</td>
      <td>${cliente.descuentoBool ? "Sí" : "No"}</td>
      <td>
        <button onclick="deleteCliente(${cliente.id})">Borrar</button>
        <button onclick="editCliente('${cliente.id}')">Editar</button>
      </td>
    `;
    tableBody.appendChild(row);
  });
}

// Mostrar/Ocultar form del cliente
document.getElementById("show-form-btn").addEventListener("click", () => {
    Swal.fire({
        title: "<strong>Agregar Cliente</strong>", html: `
        <form id="add-client-form">
        <label for="nombre">Nombre:</label>
        <input type="text" id="nombre" class="swal2-input" required><br><br>
    
        <label for="telefono">Teléfono:</label>
        <input type="number" id="telefono" class="swal2-input" required><br><br>
    
        <label for="calle">Calle:</label>
        <input type="text" id="calle" class="swal2-input" required><br><br>
    
        <label for="numero">Número:</label>
        <input type="number" id="numero" class="swal2-input" required><br><br>
    
        <label for="sector">Sector:</label>
        <input type="text" id="sector" class="swal2-input" required><br><br>
    
        <label for="descuentoBool">Descuento:</label>
        <input type="checkbox" id="descuentoBool"><br><br>
        </form>
        `,
        showCloseButton: true,
        showCancelButton: true,
        focusConfirm: false,
        confirmButtonText: `
          Agregar
        `,
        confirmButtonAriaLabel: "Agregar cliente",
        cancelButtonText: `
          Cancelar
        `,
        cancelButtonAriaLabel: "Thumbs down",
        preConfirm: () => {
            const nombre = document.getElementById("nombre").value;
            const telefono = document.getElementById("telefono").value;
            const calle = document.getElementById("calle").value;
            const numero = document.getElementById("numero").value;
            const sector = document.getElementById("sector").value;
            const descuentoBool = document.getElementById("descuentoBool").checked;
            
            if (!nombre || !telefono || !calle || !numero || !sector) {
                Swal.showValidationMessage("Por favor, completa los campos que son requeridos");
                return false;
            }
            return{nombre, telefono, calle, numero, sector, descuentoBool};
        },
      }).then((result) => {
        if (result.isConfirmed) {
            const cliente = result.value;
            console.log("Nuevo cliente", cliente);
            agregarCliente(cliente);
        }

      });
});

// Función agregar cliente
function agregarCliente(cliente){
    console.log("Hizo contacto con la función", cliente);
    fetch(`${apiURL}`,{
        method: "POST",
        headers: {
            "content-type": "application/json",
        },
        body: JSON.stringify(cliente)
    })
        .then((response) => response.json())
        .then((data) =>{
            console.log("Cliente agregado:", data);
            loadClientes();
        })
        .catch((error) => console.error("Error:", error))
}

// Función borrar cliente 
async function deleteCliente(id) {
    const result = await Swal.fire({
      title: "Estás seguro?",
      text: "No podrás recoperar estos datos!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si borrar!"
    });
  
    if (result.isConfirmed) {
      try {
        await fetch(`${apiURL}${id}/`, { method: "DELETE" });
        await loadClientes();
        Swal.fire({
          title: "Borrado!",
          text: "Este cliente fue borrado con exito.",
          icon: "success"
        });
      } catch (error) {
        console.error("Error deleting client:", error);
        Swal.fire({
          title: "Error!",
          text: "Hubo un error al borrar el cliente.",
          icon: "error"
        });
      }
    }
  }

// Función editar cliente
async function editCliente(id) {
    console.log("ID del cliente:", id);
  
    if (!id) {
      Swal.fire({
        title: "Error",
        text: "ID del cliente no válido.",
        icon: "error",
      });
      return;
    }
  
    try {
      const response = await fetch(`${apiURL}${id}/`);
      const cliente = await response.json();
  
      if (!cliente) {
        throw new Error("Cliente no encontrado");
      }
  
      console.log("Cliente recibido:", cliente);
  
      const { value: formValues } = await Swal.fire({
        title: "Editar Cliente",
        html: `
          <form id="editForm">
            <label for="nombre">Nombre:</label>
            <input id="nombre" class="swal2-input" value="${cliente.nombre || ''}">
            <label for="telefono">Teléfono:</label>
            <input id="telefono" class="swal2-input" type="number" value="${cliente.telefono || ''}">
            <label for="calle">Calle:</label>
            <input id="calle" class="swal2-input" value="${cliente.calle || ''}">
            <label for="numero">Número:</label>
            <input id="numero" class="swal2-input" type="number" value="${cliente.numero || ''}">
            <label for="sector">Sector:</label>
            <input id="sector" class="swal2-input" value="${cliente.sector || ''}">
            <label for="descuentoBool">Descuento:</label>
            <select id="descuentoBool" class="swal2-select">
              <option value="true" ${cliente.descuentoBool ? "selected" : ""}>Sí</option>
              <option value="false" ${!cliente.descuentoBool ? "selected" : ""}>No</option>
            </select>
          </form>`,
        focusConfirm: false,
        showCancelButton: true,
        preConfirm: () => {
          return {
            nombre: document.getElementById("nombre").value,
            telefono: document.getElementById("telefono").value,
            calle: document.getElementById("calle").value,
            numero: document.getElementById("numero").value,
            sector: document.getElementById("sector").value,
            descuentoBool: document.getElementById("descuentoBool").value === "true",
          };
        },
      });
  
      if (formValues) {
        const response = await fetch(`${apiURL}${id}/`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formValues),
        });
  
        if (!response.ok) {
          throw new Error("Error al actualizar el cliente");
        }
  
        Swal.fire({
          title: "Cliente Actualizado",
          text: "El cliente fue actualizado exitosamente.",
          icon: "success",
        });
        await loadClientes(); 
      }
    } catch (error) {
      console.error("Error al actualizar el cliente:", error);
      Swal.fire({
        title: "Error",
        text: "Hubo un problema al actualizar el cliente.",
        icon: "error",
      });
    }
  }
  
// Cargar clientes 
loadClientes();
