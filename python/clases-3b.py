# ==============================================
# 1. Introducción a la Programación Orientada a Objetos (POO)
# ==============================================
# La POO es un paradigma de programación que utiliza "clases" y "objetos".
# - Clase: Esquema o plantilla para crear objetos.
# - Objeto: Instancia de una clase.
# - Atributos: Características del objeto.
# - Métodos: Acciones que puede realizar el objeto.

print("\n1. Introducción a la POO")

# Ejemplo visual
print("Una clase es como un plano de una casa y un objeto es la casa construida.")

# Ejercicio:
# Piensa en 3 objetos de la vida real (ej.: silla, coche, perro).
# ¿Cuáles podrían ser sus atributos y métodos?

# silla: 
#       Atributos: color, material, ocupada, altura, peso, precio.
#       Métodos: sentarse, mover, apilar.
# coche: 
#       Atributos: marca, modelo, color, matrícula, velocidad, circulando. 
#       Métodos: arrancar, acelerar, frenar.
# perro: 
#       Atributos: nombre, raza, edad, peso, tamaño. 
#       Métodos: ladrar, correr, saltar.

# ==============================================
# 2. Clase Animal
# ==============================================
print("\n2. Ejercicio Práctico: Clase Animal")

class Animal:
    def __init__(self, nombre, especie, sonido):
        self.nombre = nombre
        self.especie = especie
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"El {self.nombre} hace {self.sonido}.")

perro = Animal("Perro", "Canino", "guau guau")
perro.hacer_sonido()
perro.sonido = "gluglugluglu"
perro.hacer_sonido()


# Ejercicio:
# Crea un objeto "gato" de la clase Animal con un sonido diferente y llama al método "hacer_sonido".

gato = Animal("Gato", "Felino", "miau")
gato.hacer_sonido()

gato.sonido = "grrrgrrr"
gato.hacer_sonido()

# ==============================================
# 3. Crear una Clase en Python
# ==============================================
print("\n3. Ejemplo de Clase en Python")

class Coche:
    def __init__(self, marca, modelo, anyo):
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo

    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")
        
    def __str__(self):
        return f"Coche {self.marca} {self.modelo} {self.anyo}"
    
mi_coche = Coche("Toyota", "Corolla", 2020)
mi_coche.arrancar()

# Ejercicio:
# Crea una clase "Bicicleta" con atributos "marca", "tipo" (montaña, carretera), "eléctrica" y "tamaño".
# Añade un método, "estado", que imprima un mensaje diciendo que la bicicleta está lista para rodar.

class Bicicleta:
    def __init__(self, marca, tipo, electrica, tamaño):
        self.marca = marca
        self.tipo = tipo
        self.electrica = electrica
        self.tamaño = tamaño
        print(f"La bicicleta {self.marca} {self.tipo} está lista para rodar.")

    def __str__(self):
        return f"Bicicleta {self.marca} {self.tipo} {self.tamaño}"

bici = Bicicleta("Orbea", "Montaña", False, "M")

garage = []
garage.append(mi_coche)
garage.append(bici)

for vehiculo in garage:
    print(vehiculo)
        

# ==============================================
# 4. Métodos especiales y Atributos
# ==============================================
print("\n4. Métodos Especiales y Atributos")

# El init es el método al que se llama al hacer una instancia de la clase

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print(f"Se ha creado una persona llamada {self.nombre} de {self.edad} años.")

# El str es el método que se utiliza al hacer el print de un objeto de la clase
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

    def cumplir_anyos(self):
        self.edad += 1 # self.edad = self.edad + 1
        print(f"{self.nombre} ha cumplido {self.edad} años.")

    def es_mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

p = Persona("Ana", 15)
print(p)

p.cumplir_anyos()

for i in range(5):
    p.cumplir_anyos()
    p.es_mayor_edad()

# Ejercicio:
# Modifica la clase Persona para añadir un método que imprima por pantalla si la persona es mayor de edad.


# ==============================================
# 5. Aplicación Real
# ==============================================
print("\n5. Ejercicio práctico: Clase Libro")

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return(f'"{self.titulo}" de {self.autor}, tiene {self.paginas} páginas.')
titulo = input("Título del libro: ")
autor = input("Autor del libro: ")
paginas = int(input("Número de páginas: "))
libro = Libro(titulo, autor, paginas)

biblioteca = []
biblioteca.append(libro)
libro = Libro("El Principito", "Antoine de Saint-Exupéry", 96)


biblioteca.append(libro)
for libro in biblioteca:
    print(libro)

# Ejercicio:
# Crea un libro con tu título y autor favorito e imprime el resumen.


# ==============================================
# 6. Concepto de Herencia
# ==============================================
print("\n6. Herencia en Clases")
# Una clase puede ser que no sea algo aislado sino que ya venga de otro objeto más general
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Cuando una clase es "sublcase" de otro y "hereda" de ésta hablamos de herencia ya que la
# clase hija tiene todo lo de la clase padre
class CocheHerencia(Vehiculo):
    def arrancar(self):
        print(f"El {self.marca} {self.modelo} está arrancando.")

mi_coche_herencia = CocheHerencia("Ford", "Fiesta")
mi_coche_herencia.arrancar()

# Ejercicio:
# Crea una clase "Moto" que herede de "Vehiculo" e implemente un método "acelerar".


# ==============================================
# 7. Clases con Herencia
# ==============================================
print("\n7. Ejercicio Práctico: Clases con Herencia")

class PersonaBase:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(PersonaBase):
    def __init__(self, nombre, edad, puesto):
        super().__init__(nombre, edad)
        self.puesto = puesto

    def mostrar_informacion(self):
        print(f"{self.nombre}, {self.edad} años, trabaja como {self.puesto}.")

empleado = Empleado("Carlos", 30, "Desarrollador")
empleado.mostrar_informacion()

# Ejercicio:
# Crea una clase "Estudiante" que herede de "PersonaBase" y añada un método para mostrar su curso.


# ==============================================
# 8. Conclusión
# ==============================================
print("\n8. Conclusión")
print("Hoy hemos aprendido sobre clases, objetos, atributos, métodos y herencia en Python.")

# Ejercicio final:
# 1. Crea una clase "Personaje" con atributos "nombre", "edad" y "rol" (por ejemplo: mago, guerrero, arquero).
# 2. Añade un método "presentarse" que imprima un mensaje con el nombre y el rol del personaje.
# 3. Crea otra clase "Objeto" con atributos "nombre" y "tipo" (por ejemplo: poción, arma, armadura).
# 4. Crea un método en "Objeto" que muestre un mensaje indicando que el objeto ha sido encontrado.
# 5. Crea instancias de ambas clases y haz que el personaje encuentre el objeto.
# 6. Muestra los mensajes por pantalla para contar una pequeña historia.
