import { peliculas } from './peliculas.js';


const apiKey = "3be066e6";
let contenedorPeliculas = document.querySelector("#peliculas")

let listaPeliculas = document.createElement("table");
if (peliculas.length == 0){
    let item = document.createElement("tr");
    item.textContent = "No hay peliculas";
    listaPeliculas.appendChild(item);
}
else{
    let cabecera = document.createElement("thead");
    cabecera.innerHTML = `<tr><th>Título</th><th>Director</th><th>Género</th><th>Poster</th></tr>`;
    listaPeliculas.appendChild(cabecera);
    peliculas.forEach(titulo => {
    fetch(`https://www.omdbapi.com/?t=${encodeURIComponent(titulo)}&apikey=${apiKey}`)
      .then(res => res.json())
      .then(data => {
        if (data.Response === "True") {
          const div = document.createElement("tr");
          div.className = "pelicula";
          div.innerHTML = `
            <td>${data.Title} (${data.Year})</td>
            <td>${data.Director}</td>
            <td>${data.Genre}</td>
            <td><img src="${data.Poster}" alt="Poster de ${data.Title}"></td>
          `
          listaPeliculas.appendChild(div)
        } else {
          console.warn(`No encontrada: ${titulo}`)
        }
      })
      .catch(err => console.error("Error al cargar película:", err));
  });
/*
else{
    for (let pelicula of peliculas){
        let item = document.createElement("tr");
        item.innerHTML = `<td>${pelicula.titulo}</td><td>${pelicula.director}</td><td>${pelicula.año}</td><td><img src="${pelicula.img}" alt="${pelicula.titulo}"></td>`;
        listaPeliculas.appendChild(item);
}
}*/
    contenedorPeliculas.appendChild(listaPeliculas)
}