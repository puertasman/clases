import { peliculas } from './peliculas.js';


const apiKey = "3be066e6";
let contenedor = document.querySelector("#peliculas")

if (peliculas.length == 0){
    contenedor.textContent = "No hay peliculas";
}
else{
    peliculas.forEach(titulo => {
    fetch(`https://www.omdbapi.com/?t=${encodeURIComponent(titulo)}&apikey=${apiKey}`)
      .then(res => res.json())
      .then(data => {
        if (data.Response === "True") {
            const col = document.createElement("div");
            col.className = "col-md-4";
    
            col.innerHTML = `
              <div class="card h-100 shadow-sm">
                <img src="${data.Poster}" class="card-img-top" alt="Poster de ${data.Title}">
                <div class="card-body">
                  <h5 class="card-title">${data.Title} (${data.Year})</h5>
                  <p class="card-text"><strong>Director:</strong> ${data.Director}</p>
                  <p class="card-text"><strong>Género:</strong> ${data.Genre}</p>
                  <p class="card-text"><strong>IMDb:</strong> ${data.imdbRating}</p>
                </div>
              </div>
            `;
            contenedor.appendChild(col);
        } else {
          console.warn(`No encontrada: ${titulo}`)
        }
      })
      .catch(err => console.error("Error al cargar película: ", err))
  })
} 