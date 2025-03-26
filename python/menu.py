usuarios = ['Juan', 'Pedro', 'María', 'Antonia']

while __name__ == "__main__":
    print("Bienvenido al menú de opciones")
    print("1.- Usuarios")
    print("2.- Añadir usuarios")
    print("3.- Eliminar usuarios")
    print("4.- Salir")
    opcion = input("Elige una opción: ")
    if opcion == '1':
        if len(usuarios) == 0:
            print("No hay usuarios")
        else:
            print(f"Hay {len(usuarios)} usuarios")
            for usuario in usuarios:
                print(usuario)
    if opcion == '2':
        usuario = input("Escribe el nombre del usuario: ")
        usuarios.append(usuario)
        print(f"Usuario {usuario} añadido")
    if opcion == '3':
        print(f"Usuarios: {usuarios}")
        usuario = input("Escribe el nombre del usuario: ")
        usuarios.remove(usuario)
        print(f"Usuario {usuario} eliminado")
    if opcion == '4':
        print("Gracias por utilizar el programa")
        break