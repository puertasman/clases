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

    li.textContent = nuevaTarea + ' ' 
    //3.1 Crear un elemento button
    let boton = document.createElement('button')
    boton.textContent = 'Eliminar'
    boton.onclick = function(){
        li.remove()
    }
    li.appendChild(boton)
    
    //4. Agregar la tarea a la lista
    document.querySelector('#listaTareas').appendChild(li)
    
    //5. Limpiar el input
    document.querySelector('#nuevaTarea').value = ''
    document.querySelector('#tareaVacia').style.display = 'none'
}
