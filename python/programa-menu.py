while __name__ == "__main__":
    print("Bienvenido al menú de opciones")
    print("1.- Jugar")
    print("2.- Opciones")
    print("3.- Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        print("Jugando")
        input("Presiona enter para continuar")
    elif opcion == "2":
        print("Modificando opciones")
        input("Presiona enter para continuar")
    elif opcion == "3":
        print("Saliendo")
        break
    else:
        print("Opción incorrecta")
