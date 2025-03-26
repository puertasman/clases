const alumnos = [
    "Elena Casado Rodríguez",
    "Hugo Chacón Galván",
    "Aarón Conejo Flores",
    "Idune del Olmo Antón",
    "Nahia Díaz Rodríguez",
    "Ibrahim El Maadioui",
    "Ricardo Figueroa Alcaide",
    "Daniel Flores Hermoso",
    "Iker Gil Corbalán",
    "Eric González Fernández",
    "Alejandro Hinojosa Bertrán",
    "Oumar Jallow",
    "Pol Lara Moratalla",
    "Héctor Lechuga Cabanillas",
    "Samuel Francisco Macías Burbano",
    "Lisset Mancera Márquez",
    "Víctor Martínez Rodríguez",
    "Laia Miralles Verdugo",
    "Naira Mogollón Requena",
    "Irene Montilla Montero",
    "Ana Muñoz Mena",
    "Marta Muñoz Mena",
    "Iker Nuevo García",
    "Lucía Ortega de Arcos",
    "Leyre Rodríguez Garrido",
    "Carolina Ros Sánchez",
    "Aisa Sillah",
    "Dereck Geovanny Valencia Sánchez",
    "Carlota Vela Sánchez",
    "Xi Kun Wang",
    "Jiquing Wang"
  ];
  


// función drop
function crearDropzone() {
    const dropzone = document.createElement("div");
    dropzone.className = "mesa dropzone";
    dropzone.addEventListener("dragover", (e) => e.preventDefault());
    dropzone.addEventListener("drop", onDrop);
    return dropzone;
  }

  function onDrop(e) {
    e.preventDefault();
    const id = e.dataTransfer.getData("text/plain");
    const nuevoAlumno = document.getElementById(id);
  
    // Si hay un alumno ya sentado, devolverlo a la lista
    if (this.children.length > 0) {
      const anterior = this.children[0];
      listaContainer.appendChild(anterior);
      ordenarLista();
    }
  
    this.appendChild(nuevoAlumno);
  }
  

// Mostrar lista de alumnos
const listaContainer = document.getElementById("lista-alumnos");

alumnos.forEach((nombre, i) => {
    const div = document.createElement("div");
    div.className = "alumno";
    div.textContent = nombre;
    div.setAttribute("draggable", "true");
    div.setAttribute("data-index", i); // <- índice original
    div.id = `alumno-${i}`;
  
    div.addEventListener("dragstart", (e) => {
      e.dataTransfer.setData("text/plain", div.id);
    });
  
    div.addEventListener("click", () => {
      if (div.parentElement !== listaContainer) {
        listaContainer.appendChild(div);
        ordenarLista();
      }
    });
  
    listaContainer.appendChild(div);
  });

  function ordenarLista() {
    const alumnosLista = Array.from(listaContainer.children);
  
    alumnosLista.sort((a, b) => {
      return parseInt(a.dataset.index) - parseInt(b.dataset.index);
    });
  
    alumnosLista.forEach(alumno => listaContainer.appendChild(alumno));
  }

const aula = document.getElementById("aula");

// 4 filas normales: 3 grupos de 2 sillas
for (let fila = 0; fila < 4; fila++) {
  const filaDiv = document.createElement("div");
  filaDiv.className = "d-flex justify-content-center mb-3";

  for (let grupo = 0; grupo < 3; grupo++) {
    const grupoDiv = document.createElement("div");
    grupoDiv.className = "d-flex mx-3"; // separación entre grupos

    for (let silla = 0; silla < 2; silla++) {
      grupoDiv.appendChild(crearDropzone());
    }

    filaDiv.appendChild(grupoDiv);
  }

  aula.appendChild(filaDiv);
}

// Última fila: grupos 2 + 3 + 2
const filaFinal = document.createElement("div");
filaFinal.className = "d-flex justify-content-center mb-3";

// Grupo 1: 2 sillas
const grupo1 = document.createElement("div");
grupo1.className = "d-flex mx-3";
grupo1.appendChild(crearDropzone());
grupo1.appendChild(crearDropzone());
filaFinal.appendChild(grupo1);

// Grupo 2: 3 sillas
const grupo2 = document.createElement("div");
grupo2.className = "d-flex mx-3";
grupo2.appendChild(crearDropzone());
grupo2.appendChild(crearDropzone());
grupo2.appendChild(crearDropzone());
filaFinal.appendChild(grupo2);

// Grupo 3: 2 sillas
const grupo3 = document.createElement("div");
grupo3.className = "d-flex mx-3";
grupo3.appendChild(crearDropzone());
grupo3.appendChild(crearDropzone());
filaFinal.appendChild(grupo3);

aula.appendChild(filaFinal);

document.getElementById("guardar-btn").addEventListener("click", () => {
    const posiciones = {};
  
    // Recorremos todas las mesas
    document.querySelectorAll(".mesa").forEach((mesa, index) => {
      if (mesa.children.length > 0) {
        const alumno = mesa.children[0];
        posiciones[`mesa-${index}`] = alumno.id; // guardamos por ID
      }
    });
  
    // Guardamos también quién está en la lista
    const enLista = Array.from(listaContainer.children).map(div => div.id);
  
    localStorage.setItem("distribucionMesas", JSON.stringify({ posiciones, enLista }));
  });

  window.addEventListener("DOMContentLoaded", () => {
    const data = JSON.parse(localStorage.getItem("distribucionMesas"));
    if (!data) return;
  
    const { posiciones, enLista } = data;
  
    // Primero vaciamos todas las mesas
    document.querySelectorAll(".mesa").forEach(mesa => {
      mesa.innerHTML = "";
    });
  
    // Restauramos los alumnos en la lista
    enLista.forEach(id => {
      const alumno = document.getElementById(id);
      if (alumno) listaContainer.appendChild(alumno);
    });
  
    // Restauramos los alumnos en sus mesas
    for (const key in posiciones) {
      const mesa = document.querySelectorAll(".mesa")[parseInt(key.split("-")[1])];
      const alumno = document.getElementById(posiciones[key]);
      if (mesa && alumno) mesa.appendChild(alumno);
    }
  });