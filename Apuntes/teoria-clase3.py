print("hola")
numero = input("Inserta un numero")
print(type(numero))

# # # ENTRADA / SALIDA DE DATOS (INPUT)
# # # La función input() nos permite pedirle información al usuario a través de la consola. 
# # # El valor que el usuario introduce se guarda siempre como un string (str), 
# # # sin importar si son números o letras.

nombre = input("¿Cómo te llamas? ")
print(f"Hola mi nombre es {nombre}")



# # # CONVERSION DE TIPOS Y ROUND

# # # int()

# # # La función int() convierte un valor a un número entero.
# # # Uso: int(valor)
# # # Tipos aceptados: Cadenas de texto que representen enteros, flotantes.
# # # Puntos a tener en cuenta:
# # # Si la cadena no puede convertirse a un entero (ej. "hola", "3.14"), lanzará un error.
# # # Si se le pasa un float, trunca la parte decimal (no redondea).

texto_entero = input("Introduce un número")
numero_entero = int(texto_entero)
print(type(texto_entero))
print(type(numero_entero))



# # # float()

# # # La función float() convierte un valor a un número de tipo float (decimal).
# # # Uso: float(valor)
# # # Tipos aceptados: Strings que representen números (enteros o decimales), enteros, ej. “2” o “1.5”.
# # # Puntos a tener en cuenta:
# # # Si la string no puede convertirse a float (ej. "abc"), lanzará un error.

texto_decimal = "3.14159"
numero_decimal = float(texto_decimal)
print(type(texto_decimal))
print(type(numero_decimal))


# # # round()

# # # La función round() en Python se utiliza para redondear números.

# # # round(numero): Redondea al entero más cercano. Si está exactamente en el medio (ej. 2.5), Python 3.x redondea al entero par más cercano (por ejemplo, 2.5 se redondea a 2, 3.5 a 4). 
# # # round(numero, ndigits): Redondea al número especificado de dígitos decimales.

print(round(3.14159))      # REDONDEO BASICO
print(round(2.7)) 

print(round(2.5))          # REDONDEO DEL BARQUERO
print(round(3.5)) 

print(round(3.14159, 2))   # REDONDEO CON NUMEROS DECIMALES




# # # CONTROL DE FLUJO

# # # BREAK Y CONTINUE
# # # Sentencias muy importantes en Python (y en muchos otros lenguajes de programación) que te dan un control preciso 
# # # sobre cómo se ejecutan los bucles (for y while). 
# # # Permiten alterar el flujo normal de iteración.

# # #break
# # # Se utiliza para terminar un bucle completamente y de forma inmediata:
numeros = [1, 5, 8, 12, 15, 20]
numero_objetivo = 12
for num in numeros:
    print(f"Comprobando el número: {num}")
    if num == numero_objetivo:
        print(f"¡Encontrado! El número {numero_objetivo} está en la lista.")
        break 
    print(f"El número {num} no es el objetivo.")
print("Fin del programa después del bucle.")


# # # continue
# # # Se utiliza para saltar la iteración actual del bucle y pasar directamente a la siguiente iteración:

numeros = [1, 2, 3, 4, 5, 6, 7]

for num in numeros:
    if num % 2 == 0: 
        print(f"Saltando el número par: {num}")
        continue

    print(f"Procesando número impar: {num} (su cuadrado es {num * num})")
print("Fin del programa después del bucle.")



# # # PRÁCTICA: Ejercicio: Filtrado de Edades en una Lista

# Crea un programa en Python que itere sobre una lista de edades. 
# Durante la iteración, debes mostrar únicamente aquellas edades que correspondan a personas mayores de 18 años. 
# Si en algún momento se encuentra una edad igual o superior a 65 años, el programa debe detener su ejecución inmediatamente


lista_edades = [15, 22, 17, 30, 65, 45, 70, 19]

for edad in lista_edades:
    if  edad >= 18 and edad < 65:
        print(edad)
    elif edad >= 65:
        print(f"Detener ejecución")
        break


# TRY/EXCEPT

# Con try/except, tú le dices a Python:

# try: Intenta ejecutar este código.
# except: Si falla (si ocurre un error), no te detengas. Ejecuta este código alternativo (para controlar o informar del error)."

try:
    resultado = 10 / 0
except:
    print("Error!!")



# PRÁCTICA: Utiliza lo aprendido hasta ahora y +

# El siguiente ejercicio debe validar lo que escriba el usuario utilizando un bucle while.

# Se deben cumplir las siguientes condiciones:

# El usuario tendrá como máximo 5 intentos para introducir un número válido.
# En cada iteración, el programa debe pedir al usuario que introduzca un número.
# Si el usuario escribe algo que no sea un número (por ejemplo, letras o símbolos), se debe mostrar un mensaje de advertencia y volver a pedir el número sin detener el programa.
# Si el usuario introduce un número válido:
# Se convierte a entero.
# Se muestra un mensaje indicando que el número es válido.
# El bucle finaliza inmediatamente

intentos = 0
max_intentos = 5

while intentos < max_intentos:
    entrada = input("Introduce un número: ")
    try:
        numero = int(entrada)                                    # Intenta convertir a entero
        print(f"Número válido. Has introducido: {numero}")
        break                                                    # Sale del bucle si el número es válido
    except:
        print("Entrada no válida. Introduce un número entero.")
        intentos += 1



# PROGRAMACION ORIENTADA A OBJETOS (POO)
# Es una forma de programar que imita el mundo real usando “objetos”.

# Es un paradigma de programación que organiza el código en torno a objetos, 
# los cuales representan entidades del mundo real y contienen tanto datos (atributos) 
# como comportamientos (métodos o funciones).


# DEFINICION DE CLASES

class Animal:                               # EN CLASES LA PRIMERA LETRA SIEMPRE EN MAYUSCULA
    def __init__(self, nombre, edad):       # Self, es el OBJETO EN ESE MOMENTO, nombre de la propiedad 
        self.nombre = nombre
        self.edad = edad
mi_animal = Animal("Simba", 1)              # Esto se llama instancia 
print(f"Mi animal se llama {mi_animal.nombre} y tiene {mi_animal.edad} año.")       #SE PONE PUNTO 


# DEFINICION DE METODOS

# Un método es una función que está dentro a una clase.

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")
mi_animal = Animal("Fido", 5)
mi_animal.hacer_sonido()

# Se invoca a través de una instancia de la clase (un objeto) usando la sintaxis objeto.metodo().
# El primer argumento es siempre una referencia al propio objeto (self).




# METODOS DE CLASE  --> CLASS METHOD, STATIC METHOD

# Operan sobre la clase en sí, no sobre una instancia específica. Se definen usando @classmethod. 

# El primer parámetro es por convención cls, que hace referencia a la propia clase. 

class Empleado:
    sueldo_base = 50000
    def __init__(self, nombre, cargo):
        self.nombre = nombre
        self.cargo = cargo
        
@classmethod
def aumentar_sueldo_base(cls):
    cls.sueldo_base += 1000
    print(f"El nuevo sueldo base es: {cls.sueldo_base}")
        
empleado1 = Empleado("Ana", "Gerente")
print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")

Empleado.aumentar_sueldo_base()
empleado2 = Empleado("Juan", "Peon")

print(f"Sueldo de {empleado1.nombre}: {Empleado.sueldo_base}")



class Matematica:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b
print(Matematica.sumar(5, 3))



# Tipo de método	Primer parámetro	Puede acceder a atributos de la clase	Puede acceder a atributos del objeto	  Cuándo usarlo
# @staticmethod	     ❌ ninguno	          ❌ No	                                   ❌ No	                             Cuando solo hace algo relacionado con la clase pero no necesita datos de ella
# @classmethod	       ✅ cls	          ✅ Sí	                                   ❌ No	                             Cuando trabajas con la clase misma (crear instancias, cambiar variables de clase)
# (método normal)	   ✅ self	          ✅ Sí	                                   ✅ Sí	                             Cuando trabajas con datos del objeto


# PRÁCTICA
# Crea una clase Producto con propiedades como nombre, precio y
# un método mostrarDetalles() que muestre por consola la información del producto.

# Crea 2 productos diferentes usando la clase que acabas de crear


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrarDetalles(self):
        print(f"Mi casa tiene una {self.nombre} que vale {self.precio} euros")

producto1 = Producto("Mesa", 565)
producto2 = Producto("Silla", 87)
producto1.mostrarDetalles()
producto2.mostrarDetalles()


# HERENCIA

# Mecanismo que permite a una clase (llamada subclase o clase hija) heredar las propiedades 
# y métodos de otra clase (llamada superclase o clase padre).

# Este mecanismo fomenta la reutilización de código y la creación de una jerarquía de clases lógicas.

# Para crear una clase hija, se especifica la clase padre entre paréntesis en la definición de la clase.

# Una clase hija puede usar todo lo que tiene la clase padre y, además, puede añadir nuevos atributos y métodos, o modificar los que hereda.

class Animal: 
    def __init__(self, nombre):
        self.nombre = nombre

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)          # SUPER SE UTILIZA PARA TRAERME LAS PROPIEDADES DE ARRIBA 
        self.raza = raza                  # PROPIEDAD NUEVA DEL HIJO
mi_perro = Perro("Fido", "Labrador")
print(mi_perro.nombre)



# SOBREESCRITURA DE MÉTODOS

# La sobreescritura (o overriding) ocurre cuando una clase hija define un método con el mismo nombre que uno de sus padres. 

# La implementación del método en la clase hija reemplaza a la de la clase padre.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    
    def hacer_sonido(self): 
        print("El perro ladra: ¡Guau!")

animal_generico = Animal("Tommy")
animal_generico.hacer_sonido() 
perro = Perro("Tommy","husky")
perro.hacer_sonido()


# EXTENSION DE UN METODO

# Extender un método significa que la clase hija añade funcionalidad al 
# método del padre en lugar de reemplazarlo por completo. 

# Esto se logra llamando al método del padre dentro del método de la clase hija.

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        print("El animal hace un sonido genérico.")

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza
    def hacer_sonido(self): 
        super().hacer_sonido()

animal_generico = Animal("Tommy")
animal_generico.hacer_sonido() 
perro = Perro("Tommy","husky")
perro.hacer_sonido()


# PRACTICA
# Hereda la clase Producto para crear una clase Electrodomestico, que tenga una propiedad adicional llamada marca y un método encender() que muestre por  consola “Encendiendo…”.
# Crea un objeto de la clase Electrodomestico


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrarDetalles(self):
        print(f"Mi casa tiene una {self.nombre} que vale {self.precio} euros")

producto1 = Producto("Mesa", 565)
producto2 = Producto("Silla", 87)
producto1.mostrarDetalles()
producto2.mostrarDetalles()

class Electrodomestico(Producto):
    def __init__(self, nombre, precio, marca):
        super().__init__(nombre, precio)
        self.marca = marca
    
    def encender(self): 
        print(f"Encendiendo... {self.nombre}")

producto1 = Producto("Mesa", 565)
producto2 = Producto("Silla", 87)
producto1.mostrarDetalles()
producto2.mostrarDetalles()

producto3 = Electrodomestico("Lavadora", 700, "Siemens")
producto3.encender()




# MODULOS

# Los módulos en Python son archivos de código que contienen definiciones de funciones, clases y variables. 

# Los módulos te ayudan a organizar el código y a mantener tus proyectos ordenados y reutilizables.


import matematicas 
print(matematicas.sumar(3,5))
print(matematicas.PI)


# O PUEDO HACER...

from matematicas import PI, sumar
print(sumar(3,5))
print(PI)


# O SI PONGO UN * ME TRAE TODO

from matematicas import *
print(sumar(3,5))
print(PI)


# LE PONGP UN ALIAS PARA NO ESCRIBIRLO TODO EL RATO SI ES LARGO

import matematicas as m
print(m.sumar(3,5))
print(m.PI)


# EL MODUL MATH VIENE YA AL INSTALAR PYTHON
import math
print(math.pi)


# REQUESTS: Modulo mas rapido para operaciones
# API: mensajero que permite que dos programas diferentes hablen entre sí.


# UTILIZAMOS EL METODO GET PARA OBTENER LA INFO DE LA API

import requests
url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()

print("posts:", data)
