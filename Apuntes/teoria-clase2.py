persona = {  #Para diccionario es corchete. Lista es []
    "nombre": "Sofia",
    "edad": 18,
    "altura": 1.70,
    "hobbies":["natación", "fútbol"]
}

if type(persona) == dict:
    print("apruebas 1")
else:
    print("suspendes 1")    


if persona["nombre"] == "Sofía": #Significa que existe una propiedad "nombre" y su valor es "Sofia"
    print("apruebas 2")
else:
    print("suspendes 2")


if persona["edad"] >= 18:
    print("apruebas 3")
else:
    print("suspendes 3")


if type(persona["altura"])== float:
    print("apruebas 4")
else:
    print("suspendes 4")


if persona["hobbies"][1] == "fútbol":
    print("apruebas 5")
else:
    print("suspendes 5")





# EJEMPLO
# Crea un diccionario en la variable llamada prueba Dicc de tal 
# modo que el siguiente código no muestre por consola'suspendes':

pruebaDicc = {
    "x": 7,            #Lo que está dentro del diccionario se llama PROPIEDAD
    "y": "hola",
    "a":{
        "b": 3
    },
    "z":[1,2, "francisco"]

}

if type(pruebaDicc) == dict:
    print("apruebas 1")
else:
    print("suspendes 1")


if pruebaDicc["x"] ==7:
    print("apruebas 2")
else:
    print("suspendes 2")


if pruebaDicc["y"] =="hola":
    print("apruebas 3")
else:
    print("suspendes 3")


if pruebaDicc["a"]["b"] == 3: #Como "b" es texto, significa que está dentro de a, entonces está dentro de un diccionario {}
    print("apruebas 4")       #Si fuera un [0], sería una lista, y crearíamos una lista.
else:
    print("suspendes 4")


if pruebaDicc["z"][1] == 2: #En este caso si es una lista
    print("apruebas 5")
else:
    print("suspendes 5")


if type(pruebaDicc["z"][2]) == str: #Tiene que ser texto porque pone str
    print("apruebas 6")
else:
    print("suspendes 6") 

#USAR PRINT SE LLAMA DEBUGGING



#BUCLES
# Secuencia de instrucciones de código que se ejecuta repetidas veces,
# hasta que la condición asignada a dicho bucle deja de cumplirse

#FOR sirve para REPETIR INSTRUCCIONES
vueltas = [1,2,3,4,5,6,7,8]   #Lista de vueltas
for vuelta in vueltas:        #Esto significa "Para cada número en la lista de vueltas, haz lo siguiente"
    print(f'Esta es la vuelta nº {vuelta}')


nombres =["Paco", "Elena", "Javi"]
for nombre in nombres:
    print(nombre)

print(nombres[1])


#WHILE : repite un bloque de código mientras se cumpla una condición; sigue hasta que la condición se vuelva falsa

vueltas = [1,2,3,4,5,6,7,8]
contador = 0
while contador <= 5: #Mientras el contador sea menor o igual a 5, tienes que mostrar:
    print(f"Estoy en la vuelta {vueltas[contador]}")
    contador += 1
    #o contador = contador +1


#PRÁCTICA

productos = [
{"nombre": "Laptop", "categoria": "Electrónica", "precio": 799.99, "stock": 25},
{"nombre": "Auriculares Bluetooth", "categoria": "Accesorios", "precio": 59.99, "stock": 50},
{"nombre": "Cámara Digital", "categoria": "Fotografía", "precio": 399.99, "stock": 10},
{"nombre": "Smartwatch", "categoria": "Relojes", "precio": 149.99, "stock": 75},
{"nombre": "Teclado Mecánico", "categoria": "Accesorios", "precio": 89.99, "stock": 30}]

#Si quiero acceder a Auriculares Bluetooth solo:
print(productos[1]["nombre"])

#Si quiero acceder a todos los nombres de la lista:
for producto in productos:
    print(producto["nombre"])

#Nombre de cada producto cuyo precio es mayor a 100:
for producto in productos:
    if producto ["precio"] >100:
        print(producto["nombre"])

#Nombre de cada producto cuyo stock es menor o igual a 25:
for producto in productos:
    if producto ["stock"] <=25:
        print(producto["nombre"])


#FUNCIONES : AUTOMATIZAR
def sum(a,b):
    return a + b
print(sum(21,11))
print(sum(1,1))

def frase():
    return "Me gusta el chocolate"
print(frase())

def saludar(nombre):
    return f"Hola {nombre}"
print(saludar("Elena"))


def greet(name, greeting="Hello"):
    if not name:
        return greeting
    else:
        return f"{greeting} {name}"

print(greet("Sofía"))
print(greet("Sofía", "Hola"))
print(greet(""))


def cuentaCaracteres(palabra):
    if type (palabra)==str:
        return (len(palabra))
    else:
        return("Debo ser ejecutada con un string")
print(cuentaCaracteres(8))
print(cuentaCaracteres("Adios"))
    

def cuentaCaracteres(palabra):
    return (len(palabra))
print(cuentaCaracteres("Vanidoso"))
    


def cuentaCaracteres(palabra):
    if type (palabra)==int:
        return ((palabra))
    else:
        return("Debo ser ejecutada con un int")
    
print(cuentaCaracteres(8))
print(cuentaCaracteres("Adios"))


#INMUTABLE
def sumar_dos(x):  #Le quiero sumar dos a x, devuelveme x sumada en 2
    return x+2
numero=5           #Mi numero es 5
sumar_dos(numero)
numero = sumar_dos(numero)
print(numero)

#MUTABLE
def agregar_elemento(lista):
    lista.append("nuevo")
mi_lista = ["uno", "dos"]
agregar_elemento(mi_lista)
print(mi_lista)


#ARGUMENTO POSICIONAL: EL ORDEN IMPORTA
def saludar(nombre, apellido):
    print(f"Hola, {nombre} {apellido}")
saludar("Elena", "Morales")
saludar("Morales", "Elena")


#ARGUMENTO NO POSICIONAL: EL ORDEN NO IMPORTA
def configurar_usuario(nombre, edad, activo=True):
    print(f"Usuario: {nombre}, Edad: {edad}, Activo: {activo}")
configurar_usuario(nombre="Elena", edad=23)
configurar_usuario(edad=40, nombre="Pedro", activo=False)


#* es args: ARGUMENTOS POSICIONALES VARIABLES acepta cualquier numero de argumento posicional
def sumar_todos(*numeros):
    print(f"Tipo de 'numeros': {type(numeros)}") #TUPLA
    total = 0
    for num in numeros:
        total += num
    return total

print(sumar_todos(1, 2, 3))
print(sumar_todos(50, 20, 30, 40, 10 ))
print(sumar_todos(5))


#** son kwargs: ARGUMENTOS NO POSICIONALES VARIABLES cualquier numero de argumento NO posicional
def configurar_perfil(**opciones_perfil):
    print(f"Tipo de 'opciones_perfil': {type(opciones_perfil)}") #LISTA
    print("Configuración del perfil:")
    for clave, valor in opciones_perfil.items():
        print(f" {clave}: {valor}")
configurar_perfil(nombre="Ana", edad=30, ciudad="Valencia")
configurar_perfil(tema="oscuro", notificaciones=True)


#FUNCION LAMBDA
# Las funciones lambda en Python son funciones anónimas, es decir, funciones sin nombre, 
# que se usan para operaciones cortas y simples. Se definen con la palabra clave lambda.

primeraLetra = lambda palabra : (palabra[0])
print(primeraLetra("Elena"))




def obtener_nombre_completo(nombre, apellido):
    return nombre + " " + apellido

def main():
    usuarios = [
        {"nombre": "Sofía", "apellido": "Pinilla"},
        {"nombre": "Luis", "apellido": "Martínez"},
    ]

    for usuario in usuarios:
        completo = obtener_nombre_completo(usuario["nombre"], usuario["apellido"])
        print(completo)

main()
































