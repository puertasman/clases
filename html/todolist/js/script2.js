function agregarTarea(){

    //1. Obtener la tarea)
    let nuevaTarea = document.querySelector('#nuevaTarea').value
    
    //2. Validar que la tarea no esté vacía
    if (nuevaTarea === ''){
        document.querySelector('#tareaVacia').style.display = 'block'
        return
    }

    //3. Crear un elemento li
    let li = document.createElement('li')
    
    let tarea = document.createElement('span')
    tarea.innerHTML = '📋'
    li.appendChild(tarea)

    let textoTarea = document.createTextNode(' ' + nuevaTarea + ' ');
    li.appendChild(textoTarea)

    //3.1 Crear un elemento button
    let eliminar = document.createElement('i')
    eliminar.className = 'fa-regular fa-trash-can'
    eliminar.onclick = function(){
        li.remove()
    }
    li.appendChild(eliminar)
    
    //4. Agregar la tarea a la lista
    document.querySelector('#listaTareas').appendChild(li)
    
    //5. Limpiar el input
    document.querySelector('#nuevaTarea').value = ''
    document.querySelector('#tareaVacia').style.display = 'none'
}

function detectarEnter(event) {
    if (event.key === 'Enter') {
        agregarTarea();
    }
}