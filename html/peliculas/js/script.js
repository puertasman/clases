import { peliculas } from './peliculas.js';

let contenedorPeliculas = document.querySelector("#peliculas")

let listaPeliculas = document.createElement("ul");
for (let pelicula of peliculas){
    let item = document.createElement("li");
    item.textContent = pelicula.titulo;
    listaPeliculas.appendChild(item);
}
contenedorPeliculas.appendChild(listaPeliculas);