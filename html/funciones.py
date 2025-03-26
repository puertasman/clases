# Archivo de teoría y ejercicios para aprender funciones en Python
# ============================
# Teoría
# ============================
# Pequeño repaso de la sintaxis básica
#
# La indentación obligatoria, la indentación es la separación desde el margen al código
# Todo el código en Python siempre que sea básico va pegado al margen izquierdo
# Pero Python utiliza indentación para definir bloques de código.
# Normalmente, se usa una tabulación o cuatro espacios por nivel.
#
# Sensibilidad a las mayúsculas y minúsculas
# Python diferencia entre variable y Variable.
# 
# Para entender el código es bueno poner comentarios
# Si son de una línea lo hacemos con la almohadilla #
# Si es multilínea con tres comillas para abrir y tres para cerrar """ """
#
# Declaración de variables
# No es necesario declarar tipos explícitamente; Python es dinámico.
#
# Uso de operadores
# Asignación: = pone lo que hay en la parte derecha en lo que hay en la izquierda, debe ser una variable
# Aritméticos: +, -, *, /, // (división entera), % (módulo).
# Comparación: ==, !=, <, >, <=, >=.
#
#
# 1. FUNCIONES EN PYTHON
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Las funciones ayudan a evitar repetir código, mejoran la legibilidad y facilitan el mantenimiento.
#
# Sintaxis de una función:
# Siempre empezamos por la palabra del y el nombre
# y paréntesis dónde pasamos los parámetros que son opcionales
# pero si hay parámetros hay que hacer la llamada con parámetros
# def nombre_funcion(parametros_opcionales): 
#     """
#     Descripción breve de lo que hace la función.
#     """
#     # Código de la función
#     return valor_opcional
# El return es opcionales y por eso hay algunas funciones que sólo se utilizan para modificar datos
# o generar cierta información pero no devuelven nada
#
# A veces tenemos una función que necesita un parámetro pero no sabemos si nos lo van a pasar
# en ese caso le ponemos un parámetro por defecto haciendo la llamada y dando un valor
# al parámetro
# del nombre_funcion(nombre=“Amigo”):
# en este caso si llamamos a la función sin parámetro utilizará la palabra Amigo
#
# Para llamar a la función escribimos su nombre y paréntesis con los parámetros necesarios
# nombre_funcion()
# ============================
# Ejemplo 1: Función sin parámetros
# Esta función imprime un mensaje de saludo.
# ============================

def saludar():
    """Imprime un mensaje de saludo."""
    print("¡Hola! Bienvenido al mundo de Python.")

# Llamada a la función
saludar()

# ============================
# Ejemplo 2: Funciones con parámetros y retorno
# Esta función calcula el área de un rectángulo.
# ============================

def calcular_area(base, altura):
    """Calcula el área de un rectángulo dado su base y altura."""
    return base * altura

# Llamadas a la función
print("El área es:", calcular_area(5, 10))  # Devuelve 50
print("El área es:", calcular_area(8, 3))   # Devuelve 24

# ============================
# Ejercicios
# ============================
# Instrucciones: Completa las funciones para resolver los ejercicios.

# ============================
# Ejercicio 1: Calcular el doble de un número
# Crea una función que reciba un número como parámetro y devuelva su doble.
# Ejemplo: calcular_doble(4) -> 8
# ============================
# el pass que hay en todas las funciones es para que no haga nada, debemos quitarlo

def calcular_doble(numero):
    # TODO: Completa el código para devolver el doble del número
    pass

# Llamadas de prueba
#print(calcular_doble(4))  # Debería devolver 8
#print(calcular_doble(7))  # Debería devolver 14

# ============================
# Ejercicio 2: Convertir grados Celsius a Fahrenheit
# Crea una función que reciba una temperatura en grados Celsius y la convierta a Fahrenheit.
# Usa la fórmula: Fahrenheit = (Celsius * 9/5) + 32
# Ejemplo: celsius_a_fahrenheit(0) -> 32.0
# ============================

def celsius_a_fahrenheit(celsius):
    # TODO: Completa la fórmula de conversión
    pass

# Llamadas de prueba
#print(celsius_a_fahrenheit(0))   # Debería devolver 32.0
#print(celsius_a_fahrenheit(25))  # Debería devolver 77.0

# ============================
# Ejercicio 3: Determinar si un número es positivo, negativo o cero
# Crea una función que reciba un número y devuelva "Positivo", "Negativo" o "Cero" según corresponda.
# Ejemplo: evaluar_numero(-3) -> "Negativo"
# ============================

def evaluar_numero(numero):
    # TODO: Escribe las condiciones para evaluar el número
    pass

# Llamadas de prueba
#print(evaluar_numero(10))  # Debería devolver "Positivo"
#print(evaluar_numero(-3))  # Debería devolver "Negativo"
#print(evaluar_numero(0))   # Debería devolver "Cero"

# ============================
# Ejercicio 4: Repetir un mensaje
# Crea una función que reciba un mensaje y un número, y devuelva el mensaje repetido ese número de veces.
# Ejemplo: repetir_mensaje("Hola", 3) -> "HolaHolaHola"
# ============================

def repetir_mensaje(mensaje, veces):
    # TODO: Devuelve el mensaje repetido el número de veces indicado
    pass

# Llamadas de prueba
#print(repetir_mensaje("Hola", 3))  # Debería devolver "HolaHolaHola"
#print(repetir_mensaje("Python", 2))  # Debería devolver "PythonPython"

# ============================
# Ejercicio 5: Saludo personalizado
# Crea una función que reciba un nombre y devuelva un saludo personalizado.
# Ejemplo: saludo_personalizado("Enrique") -> "Hola, Enrique!"
# ============================

def saludo_personalizado(nombre):
    # TODO: Devuelve un mensaje que salude al nombre proporcionado
    pass

# Llamadas de prueba
#print(saludo_personalizado("Enrique"))  # Debería devolver "Hola, Enrique!"
#print(saludo_personalizado("Marta"))    # Debería devolver "Hola, Marta!"

# ============================
# Ejercicio 6: Crear un eco interactivo
# Crea una función que reciba un mensaje y un número, y devuelva el mensaje repetido con un separador.
# Por ejemplo, un chatbot que devuelve el mensaje separado por guiones (-).
# Ejemplo: eco_interactivo("Hola", 3) -> "Hola-Hola-Hola"
# ============================

def eco_interactivo(mensaje, veces):
    # TODO: Devuelve el mensaje repetido el número de veces con un separador "-"
    pass

# Llamadas de prueba
#print(eco_interactivo("Hola", 3))  # Debería devolver "Hola-Hola-Hola"
#print(eco_interactivo("Python", 2))  # Debería devolver "Python-Python"

# ============================
# Ejercicio 7: Par o impar
# Crea una función que reciba un número y devuelva el texto par o impar
# Ejemplo: par_impar(33) -> impar
# Para esto nos hace falta utilizar un condicional (if)
# ============================

def par_impar(numero):
    # TODO: Devuelve par o impar en función del valor del número
    pass

# Llamadas de prueba
#print(par_impar(26))  # Debería devolver "Par"
#print(par_impar(37))  # Debería devolver "Impar"

# ============================
# Ejercicio 8: Media de tres números
# Crea una función que reciba tres números y devuelva la media
# Ejemplo: media(2,4,6) -> 4
# ============================

def media(num1, num2, num3):
    # TODO: Devuelve la media de los tres valores
    pass

# Llamadas de prueba
#print(media(2,4,9))  # Debería devolver "5"
#print(media(-9,17,13))  # Debería devolver "7"

# ============================
# Ejercicio 9: Sin guía
# Crea una función que reciba dos números y devuelva el mayor de ellos.
# Instrucciones:
# - Define tanto el encabezado como el cuerpo de la función.
# - Realiza al menos dos llamadas de prueba con diferentes valores.
# Ejemplo:
# mayor(10, 20) -> 20
# mayor(-5, 3) -> 3
# ============================
