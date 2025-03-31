# importamos el módulo random para poder hacer cosas de manera aleatoria
import random

nombres = ["Juan", "Pedro", "Luis", "Ana", "Maria", "Sara", "Lucia", "Pablo", "Javier", "Raul", "David", "Carlos", "Sergio", "Jorge", "Marta", "Elena", "Carmen", "Rosa", "Laura", "Isabel"]


apellidos = ["Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Alvarez", "Romero", "Alonso", "Gutierrez", "Navarro"]

#creamos la clase Persona
class Persona:
    # inicializador __init__
    def __init__(self):
        self.nombre = random.choice(nombres)
        self.apellido = random.choice(apellidos)
        self.edad = random.randint(15,20)
        self.peso = random.randint(50,80)
        print(f"Se ha creado la persona {self.nombre} {self.apellido} y tiene {self.edad} años.")

    # redefinimos el __str__ cadena que sale cuando llamo al prin del objeto
    def __str__(self):
        return f"{self.apellido}, {self.nombre} de {self.edad} años."

    def comer(self, cantidad):
        self.peso += cantidad / 1000
        print(f"{self.nombre} ha comido {cantidad} gramos y ahora pesa {self.peso}")

# para crear un objeto hay que llamar a la clase

# creamos la lista para guardar personas
personas = []

for i in range(20):
    # crea 20 personas, la i coge valores desde 0 hasta 19
    personas.append(Persona())

for persona in personas:
    print(persona)

random.choice(personas).comer(300)