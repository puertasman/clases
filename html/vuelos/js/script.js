import {vuelos} from './vuelos.js'
let ordenActual = ''
let ordenAscendente = true
let filtro = ''
// comprobamos que ha importado los vuelos
// console.log(vuelos[0])

// Ahora toca trabajar con todos los vuelos
// Primero vamos a ver si somos capaces de poner todos los vuelos al final del documento que
// vamos a añadir cada elemento como p como hijo de body
function cargarDatos(vuelos){
    const tabla = document.querySelector('#tablaVuelos');
    tabla.innerHTML = ''; 
    let vuelosFiltrados
    if (filtro === ''){
        vuelosFiltrados = vuelos
    }
    else{  
        vuelosFiltrados = vuelos.filter(vuelo => vuelo['compania'].toLowerCase().includes(filtro.toLowerCase()))
    }
    if ( ordenActual !== ''){
        vuelosFiltrados = [...vuelosFiltrados].sort((a, b) => {
        if (typeof a[ordenActual] === "string") {
          return a[ordenActual].localeCompare(b[ordenActual]);
        } else {
          return a[ordenActual] - b[ordenActual]
        }
    })
    }
    if (!ordenAscendente) {
        vuelosFiltrados = vuelosFiltrados.reverse() 
    }

    let listaIconos = [...new Set(vuelosFiltrados.map(vuelo => vuelo['compania']))]
    listaIconos = [...listaIconos].sort()
    let imgIconos = document.querySelector('#companiesLogos')
    imgIconos.innerHTML = ''
    for (let icono of listaIconos){
        let img = document.createElement('img')
        img.onclick = function(){
            filtro = icono
            document.querySelector('#companiaInput').value = ''
            cargarDatos(vuelos)
        }
        img.filtro = icono
        img.src = 'img/' + icono + '.png'
        imgIconos.appendChild(img)
    }

    if (vuelosFiltrados.length === 0) {
        tabla.innerHTML = '<tr class="align-middle"><td colspan="4" class="sinResultados">No se encontraron resultados</td></tr>';
    }

    for (let vuelo of vuelosFiltrados){
        let tr = document.createElement('tr')
        
        let td = document.createElement('td')
        tr.classList.add('align-middle')
        td.textContent = vuelo['hora']
        tr.appendChild(td)
        
        let td2 = document.createElement('td')
        let logo = document.createElement('img')
        logo.classList.add('logo')
        logo.src = 'img/' + vuelo['compania'] + '.png'
        td2.appendChild(logo)
        let text = document.createElement('span')
        text.textContent = vuelo['compania']
        td2.appendChild(text)
        tr.appendChild(td2)

        let td3 = document.createElement('td')
        td3.textContent = vuelo['destino']
        tr.appendChild(td3)

        let td4 = document.createElement('td')
        let horas = Math.floor(vuelo['duracion'] / 60)
        let minutos = vuelo['duracion'] % 60
        td4.textContent = horas + 'h ' + minutos + 'm'
        tr.appendChild(td4)

        tabla.appendChild(tr)
    }
}

cargarDatos(vuelos);

// el filtro
document.querySelector('#companiaInput').addEventListener('input', function(){
    filtro = this.value
    cargarDatos(vuelos)
})

let sortIcons = document.querySelectorAll('.sort-icon');

sortIcons.forEach(icon => {
    icon.addEventListener('click', function () {
        const column = this.getAttribute('data-column');
        ordenarPorColumna(column); 
    });
});

function ordenarPorColumna(columna) {
    if (ordenActual === columna) {
        ordenAscendente = !ordenAscendente
    } else {
        ordenAscendente = true
        ordenActual = columna
    }
    cargarDatos(vuelos)
  }

function borrarFiltros(){
    filtro = ''
    document.querySelector('#companiaInput').value= ''
    cargarDatos(vuelos)
}

document.querySelector('#borrarFiltros').addEventListener('click', borrarFiltros)