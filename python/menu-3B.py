usuarios = ['José', 'María', 'Juan', 'Ana']

while __name__ == "__main__":
    print("Esto es mi primer menú")
    print("1. Listar usuarios")
    print("2. Añadir usuarios")
    print("3. Borrar usuarios")
    print("4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        if len(usuarios) == 0:
            print("No hay usuarios")
        else: 
            print(f"La lista tiene {len(usuarios)} usuarios")
            for usuario in usuarios:
                print(usuario)
    if opcion == "2":
        nombre = input("Cómo se llama el nuevo usuario? ").strip().lower().capitalize()
        # strip quita espacios en blanco al principio y al final
        # lower convierte a minúsculas
        # capitalize convierte la primera letra en mayúsculas
        usuarios.append(nombre)
        print(f"El usuario {nombre} ha sido añadido")
    if opcion == "3":
        nombre = input("Cómo se llama el usuario a borrar? ").strip().lower().capitalize()
        if nombre in usuarios:
            usuarios.remove(nombre)
            print(f"El usuario {nombre} ha sido borrado")
        else:
            print(f"El usuario {nombre} no existe")
    if opcion == "4":
        print("Gracias por utilizar este programa")
        break