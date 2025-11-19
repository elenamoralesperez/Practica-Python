print("hola python!!!") #Uso print con comillas para escribir texto

nombre:str="Pepe" #nombre es el nombre de la variable y str significa texto. El = es para asignar el valor
edad_ejemplo:int=7 #int significa numero entero y float es para decimales

nombre:str="Elena" #creo las variables de texto
apellido:str="Morales Pérez"
ciudad:str="Yecla"
edad:int=23

print(nombre)
print(apellido)
print(ciudad)
print(edad)

mensaje = f"Hola, me llamo {nombre} y mi apellido es {apellido}"
print(mensaje)

vivo:bool= True #bool es para condiciones de true or false

tengo_carnet:bool= True
print(tengo_carnet)

print(nombre.upper()) #MAYUSCULAS
print(apellido.lower()) #MIINUSCULAS
print(nombre[0]) #Muestra la primera letra de mi nombre
print(apellido[2]) #Muestra la tercera letra de mi apellido. Como empieza a contar desde cero, la tercera letra es el numero 2
print(apellido[12])
print(nombre[-1]) #Empieza a contar desde atrás el nombre por lo que me da la ultima letra de mi nombre
print(len(nombre)) #Contar cuantas letras tiene mi nombre

persona = { #creo una variable para crear un DICCIONARIO para que se guarde y usarlo siempre
    #ya no se pone el igual, sino los : por ser diccionario
    "nombre": "Javi",
    "edad": 27,
    "altura": 1.80,
    "tiene_carnet": True
}
print(persona)
print(persona[nombre]) #acceder a un valor --> Si quiero que me muestre solo el nombre pongo su variable y la variable madre del diccionario que en este caso seria persona
print(persona["nombre"], persona["altura"]) #si quiero que me muestre dos caracteristicas del diccionario

print(persona["edad"]) #27
persona["edad"]= 7 #modificar valor --> ahora en edad me va a salir 7 porque esto lo hago para modificar la edad de 27
del persona ["altura"] #eliminar propiedad

diccionario: dict[str, int | float | str | bool] = { #significa tipar el diccionario, no repercute en nada pero queda bonito
    "nombre": "Elena",
    "edad": 23,
    "ciudad": "Yecla",
    "soltera": False
}
print(diccionario)
print(diccionario["nombre"])

frutas = ["manzana", "pera", "platano"] #lista es coleccion ordenada y modificable de elementos
print (frutas[1]) #cada elemento de una lista tiene un índice y empieza a contar desde cero como las strings


diccionarioejemplo = [
    {
        "nombre": "Elena",
        "edad": 23
    },
    {
        "nombre": "Carla",
        "edad": 22,
    }
]
print (diccionarioejemplo[1]["nombre"]) #Me dice el segundo nombre

#AÑADIR PARTE QUE ME FALTA CON EJEMPLO CORREO SOFI


listacompra = ["pan", "leche", "huevos"] #creo una lista
listacompra.append("frutas") #se añade al final
listacompra.insert(2, "verduras") #se añade por posicion, en este caso segunda posicion
listacompra.pop(-1) #se elimina por posicion
print(listacompra)

#Una TUPLA es una colección ordenada e INMUTABLE de elementos.
#Dato mutable, lo puedo cambiar, y dato inmutable no lo puedo cambiar
#Ejemplo de como tipar una tupla: tuple[str, int, bool] =(“Javi", 30, True)

#Una constante es una variable que no debería cambiar su valor una vez definida.

#NO SE PUEDE SUMAR UN STRING CON UN NUMERO 


#OPERADORES

#En los aritmeticos, el % modulo es para el resto. Si el numero es par, el resto es cero
#== Igual> → Mayor que, si pongo solo un = estoy creando una variable
#!= es que NO sea igual por ejemplo, 1!= 1 --> FALSE

edad = 23
print(edad>= 23)

#OPERADORES LOGICOS: and, or, not,

nombre = "Elena"
edad = 17
print(edad >= 18 and nombre == 'Elena') #TRUE
print(not edad >= 18 and nombre == 'Elena') #FALSE

nombre = "Elena"
print("a" in nombre) #me busca que tenga una a --> TRUE. IN ES QUE INCLUYA
print("z" not in nombre) #me busca que tenga una z --> FALSE. NOT IN QUE NO ESTE INCLUIDO
frutas = ["manzana", "pera", "plátano"]
print("pera" in frutas)
print("kiwi" not in frutas)


# = asigna un valor. Ejemplo: a = 1
# += suma un valor y lo asigna. Ejemplo: a += 2 // a = a + 2
# -= resta un valor y lo asigna. Ejemplo: a -= 2 // a = a – 2
# *= multiplica y asigna.Ejemplo: a *= 2 // a = a * 2
# /= divide y asigna.Ejemplo: a /= 2 // a = a / 2
# %= calcula el resto y lo asigna. Ejemplo: a %= 2 // a = a % 2


#CONDICIONALES. Una expresión que se evalúa como true o false.
age = 18
if age >= 18: #SI TIENES 18...
    print("Eres mayor de edad")
else: #SI NO TIENES LOS 18...
    print("Eres menor de edad")

culpable = True
if culpable:
    print("Workalcoholic")
else:
    print("Not workalcoholic")


# #Sentencia else if
# Use la declaración else if para especificar una nueva condición si la primera condición es falsa.

# if condition1:
# bloque de código que se ejecutará si condition1 es true
# elif: condition2
# bloque de código que se ejecutará si condition1 es false y condition2 es true
# else:
# bloque de código que se ejecutará si condition1 es false y condition2 es false

person = {
    "age": 17,
    "sonOfBoss": True
}
if person["age"] >= 18:
    print("Eres mayor de edad")
elif person["sonOfBoss"] == True:
    print("No eres mayor de edad, pero eres el hijo del jefe")
else:
    print("Eres menor de edad")
