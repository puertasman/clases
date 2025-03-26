lista = [1, 2 , 3, 4]

let colocarLista = document.querySelector('#lista')
for ( let item of lista){
    li = document.createElement('li')
    li.textContent = item
    colocarLista.append(li)
}

