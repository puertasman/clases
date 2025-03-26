import { peliculas } from './peliculas.js';

let contenedorPeliculas = document.querySelector("#peliculas")

let listaPeliculas = document.createElement("table");
if (peliculas.length == 0){
    let item = document.createElement("tr");
    item.textContent = "No hay peliculas";
    listaPeliculas.appendChild(item);
}
else{
    for (let pelicula of peliculas){
        let item = document.createElement("tr");
        item.innerHTML = `<td>${pelicula.titulo}</td><td>${pelicula.director}</td><td>${pelicula.año}</td><td><img src="${pelicula.img}" alt="${pelicula.titulo}"></td>`;
        listaPeliculas.appendChild(item);
}
}
contenedorPeliculas.appendChild(listaPeliculas);