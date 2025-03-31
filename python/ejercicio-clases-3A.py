import random
# la libreria random permite obtener valores al azar o elementos de una lista al azar
# Las clases se definen con class y el nombre en mayúsculas

nombres = ["Juan", "Pedro", "Luis", "Ana", "Maria", "Sara", "Lucia", "Pablo", "Javier", "Raul", "David", "Carlos", "Sergio", "Jorge", "Marta", "Elena", "Carmen", "Rosa", "Laura", "Isabel"]

apellidos = ["Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Alvarez", "Romero", "Alonso", "Gutierrez", "Navarro"]

class Persona:
    # método init, creación de objeto
    def __init__(self):
        # atributos, nombre, apellidos, edad
        self.nombre = random.choice(nombres)
        # elige un nombre al azar de la lista nombres
        self.apellidos = random.choice(apellidos) 
        self.edad = random.randint(15,20)
        self.peso = random.randint(50,80) 
        print(f"Se ha creado la persona {self.nombre} {self.apellidos} de {self.edad} años")

    # sobreescribimos el metodo str
    def __str__(self):
        return f"{self.nombre} {self.apellidos}, edad {self.edad} años."

    # función cumplir años, cambia la edad y muestra la información
    def cumplir_anyos(self):
        self.edad += 1
        print(f"{self.nombre} acaba de cumplir años, ahora tiene {self.edad}")

    # función comer, cambia el peso de la persona
    def comer(self, cantidad):
        self.peso += cantidad/1000
        print(f"{self.nombre} acaba de comer {cantidad} gramos, ahora pesa {self.peso}.")


personas = []
# lista personas para guardar personas
for i in range (20):
    # se ejecuta 20 veces, de 0 a 19
    personas.append(Persona())

for persona in personas: # coge cada elemento de la lista como persona
    print(persona) # imprime la información de la persona

random.choice(personas).cumplir_anyos()
random.choice(personas).comer(500)