# EJERCICIO 1

# RECORDAMOS QUE Un método es una función que está dentro a una clase
class CuentaBancaria:
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
    
# Metodo depositar(cantidad) que sume al saldo ---> CONDICIONAL
    def depositar(self,cantidad):
        if cantidad <= 0:
            print(f"La cantidad a depositar debe ser mayor que 0")
        else:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad:.2f}€. Nuevo saldo: {self.saldo:.2f}€")

#Metodo mostrar() que devuelva str
    def mostrar(self):
        return (f"Titular: {self.titular}, Saldo: {self.saldo: .2f}€")
    

cuenta = CuentaBancaria("Elena", 20.00)
cuenta.depositar(-1)
cuenta.depositar(12)
print(cuenta.mostrar())



# EJERCICIO 2

# PROGRAMA = INPUT

try:
    numerador = int(input(f"Introduce numerador: "))
    denominador = int(input(f"Introduce denominador: "))
    resultado = numerador / denominador
except ZeroDivisionError:
    print(f"No se puede dividir por cero")
else: 
    print(f"Resultado: {resultado}")



# EJERCICIO 3
# Haz una petición GET a la API pública: https://api.agify.io?name=sofia
# Esta API devuelve una predicción de edad promedio según el nombre

# Tu programa debe:
    # 1. Hacer la petición con requests.get()
    # 2. Convertir la respuesta a formato JSON
    # 3. Mostrar por consola:
        # - El nombre
        # - La edad estimada
        # - El número de registros usados para calcularla
    # 4. Si ocurre algún error de conexión, mostrar un mensaje: "No se pudo conectar con la API"

import requests

url = "https://api.agify.io?name=sofia"

try:
                        #response = requests.get(url, timeout = 10)
#Usa la librería requests para hacer una petición HTTP GET a una dirección (url)
# timeout=10 significa que espera como máximo 10 segundos la respuesta del servidor
# Si no responde en ese tiempo, se genera un error de tiempo de espera
# Si todo va bien, la variable response guarda la respuesta de la API (con su código de estado, contenido, cabeceras, etc.)
    response = requests.get(url, timeout = 10)
                        # response.raise_for_status()
# Este método verifica si la respuesta del servidor fue exitosa
# Si el código de estado (status code) está entre 200 y 299, todo bien → no pasa nada
# Si el código es de error (por ejemplo, 404, 500, etc.), entonces se lanza una excepción (HTTPError).
    response.raise_for_status()

    data = response.json()     # Convierte el texto JSON de la respuesta de la API en un diccionario de Python
    
    nombre = data.get("name")  # Estas lineas extraen cada dato del diccionario
    edad = data.get("age")
    registros = data.get("count")

    print("Nombre: ", nombre)
    print("Edad estimada: ", edad)
    print("Número de registros: ", registros)

except requests.exceptions.RequestException:
    print(f"No se pudo conectar con la API")
except ValueError:
    print(f"La respuesta no es un JSON valido")


# JSON significa JavaScript Object Notation, o sea, Notación de Objetos de JavaScript
# Es un formato de texto universal para intercambiar datos entre programas, muy usado en la web
#Las APIs suelen responder en formato JSON para enviar información estructurada (como si fueran “diccionarios” de Python)


# Te lo encontrarás mucho en el futuro: la librería random, 
# muy utilizada para generar números o resultados aleatorios, o "pseudoaleatorios", 
# ya que en verdad funcionan internamente en base a algoritmos 
# (es decir, no salen de la nada, sino que Python usa unos cálculos internos para crearlos)

# random.random() --> Genera un número decimal aleatorio entre 0.0 y 1.0 (sin incluir el 1.0)

import random

x = random.random()
print(x)            #0.9559387234807372


# random.randint(a, b) --> Devuelve un número entero aleatorio entre a y b, incluyendo ambos extremos

import random

x = random.randint(1, 6)
print(x)                  # 5


# random.randrange(inicio, fin, paso)
# Devuelve un número entero aleatorio dentro de un rango, pero:
# - inicio: valor desde donde empieza el rango (incluido)
# - fin: valor hasta donde llega (no incluido)
# - paso: intervalo entre números posibles (opcional)

import random

x = random.randrange(0, 10)        # números entre 0 y 9
y = random.randrange(0, 10, 2)     # números pares entre 0 y 9
print(x, y)                        # 9 y 6


# random.choice(lista) --> Devuelve un elemento aleatorio de una lista (o tupla, cadena...)

import random

colores = ["rosa", "negro", "blanco", "amarillo"]
x = random.choice(colores)
print(x)                      # amarillo


# random.shuffle(lista) --> Desordena los elementos de una lista en su lugar (no crea una nueva lista)

import random

cartas = ["A", "K", "Q", "J", "10"]
random.shuffle(cartas)
print(cartas)               # ['A', 'K', 'Q', '10', 'J']



# import random 
# help(random) 
# En los notebooks puedes conocer la documentación sobre una librería, función, módulo, etc., utilizando ??



# EJERCICIO 4

import random

lista = ['montaña', 'jardín', 'viento', 'fuego', 'corazón']

palabraAleatoria = random.choice(lista)

numero_de_vidas = 3
while numero_de_vidas > 0:
    intento = input(f"Adivinar palabra secreta: ")

    # Comprobar acierto
    if intento == palabraAleatoria:
        print(f"Enhorabuena! Has acertado! La palabra secreta es {palabraAleatoria}")
        break
    else:
        numero_de_vidas -= 1
        print(f"Incorrecto! La palabra {intento} no es la palabra secreta. Te quedan {numero_de_vidas} intentos")
    
    # Si no aciertas en los 3 intentos
else:
    print(f"Los intentos se han agotado! La palabra secreta es {palabraAleatoria}")



# EJERCICIO 5

# Utilizaremos ahora la función randint de la librería random, que devuelve un número integer, 
# seleccionado del rango especificado como argumento (start y stop)

objetivo = random.randint(15,25)

# Inicializamos total y numero de intentos
total = 0
intentos = 5

# Bucle mientras quedan intentos y no hayamos llegado al objetivo
while intentos > 0 and total < objetivo:
    try:
        numero = int(input(f"Introduce un numero entre 1 y 5: "))
    except ValueError:
        print("Por favor, introduce un numero valido")
        continue

# Comprobar que el numero esta en el rango valido
    if 1 <= numero <= 5:
        total += numero
        intentos -= 1
        print(f"Total: {total}, Intentos restantes: {intentos}")
    else: 
        print("Numero fuera de rango, intentalo de nuevo")

# Comprobar si se superó el objetivo
if total >= objetivo:
    print(f"Bravo! Has superado el objetivo!")
else:
    print(f"Oh no! Te has quedado sin intentos. Prueba otra vez")
    