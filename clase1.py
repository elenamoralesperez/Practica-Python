# EJERCICIO 1

nombreCalle = "Fernando Peligro"
numeroCalle = str(17)              #str es para texto
nombreCiudad = "Murcia"
codigoPostal = str(28001)

direccion = nombreCalle + "" + str(numeroCalle) + nombreCiudad + "" + str(codigoPostal)
print(direccion)

cadenaTexto = "Me gusta el 'deporte'"
print(cadenaTexto)
print(f'Esta cadena tiene {len(cadenaTexto)} caracteres')  #len cuenta cuantas letras tiene




# EJERCICIO 2: Que variables estan mal escritas y por que

mi_variable = "Economía"
print(mi_variable)

# otra_var = "Ejercicio --> MAL, LE FALTA COMILLA FINAL

# True = "Ejercicio" --> MAL, UTILIZA TRUE Y NO SE PUEDE USAR COMO NOMBRE DE VARIABLE (PALABRA RESERVADA)

# mi var1iable = "Alpha" --> MAL, LAS VARIABLES NO LLEVAN ESPACIOS Y USA EL NUMERO 1 PARA SUSTITUIR LA LETRA L

# import = 40 --> MAL, IMPORT TAMBIEN ES PALABRA RESERVADA

# 81mi_variable = "Agua" --> MAL, NO PUEDE COMEZAR POR NUMERO

mi_variable10 = 6           #Bien, empieza con letras, el numero va al final y no usa palabras reservadas
print(mi_variable10)



# EJERCICIO 3

añosCotizados:int=2  # numero entero
peso:float=52.3      # numero decimal
print(añosCotizados)
print(peso)

nueva = añosCotizados + peso
print(nueva)
print("La nueva variable es", type(nueva))  # Para saber que tipo de variable es con TYPE

del(añosCotizados, peso)                    # Borramos las variables con DEL




# EJERCICIO 4: OPERADORES

# 1. ARITMETICOS (+, -, *, /, %)
a = 10
b = 3

#SIEMPRE PONEMOS LA COMA DESPUES DE LAS COMILLAS
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplica:", a * b)
print("Divide:", a / b)
print("Modulo:", a % b)    # Resto de la división

print("Resultado:", (a + b)*2 -5)
print("Division Entera:", a // b)         # Ver cuantas veces cabe b en a
print("Raiz Cuadrada de 10:", a**0.5)     # Calculamos raiz cuadrada de a elevandola con doble **
print("Potencia:", a**b)                  # Potencia de 10 elevado a 3     


# 2. COMPARACION (==, !=, <, >, >=, <=)

print("a == b?", a ==b)
print("a != b?", a !=b)                   # Si a es distinto de b
print("a>b?", a >b)
print("b<=a?", b<=a )
print("(a+5) >= (b*2)?", (a+5) >= (b*2))


# 3. LÓGICOS (and, or, not)

print("(a>5) and (b<5)?", (a>5) and (b<5))
print("(a<5) or (b<5)?", (a<5) or (b<5))
print("not(a==b)?",not(a==b))
print("(a > 5) and not (a == 10)?", (a > 5) and not (a == 10))


#CAMBIAMOS DE VARIABLES

A = 4
B = "Text"
C = 4.1

print(A==B)
print(A != C)     #NO son equivalentes es !=
print(A > C)
print(C <= A) 
print(B != C)


# 4. PERTENENCIA (in, not in)

numerosLista = [1,2,3,4,5]
print("3 in numerosLista?", 3 in numerosLista)
print("6 in numerosLista?", 6 not in numerosLista)

texto:str="python"                       # variable STRING que pone de texto python
print("'y' in texto?", 'y' in texto)     # utilizamos la doble comilla!!
print("'z' in texto?", 'z' not in texto)


# ASIGNACIÓN 

x = 10
print("x:", x)
x += 5
print("x += 5:", x)
x -= 3
print("x -= 3:", x)
x *= 2
print("x *= 2:", x)
x /= 4
print("x /= 4:", x)
x %= 3
print("x %= 3:", x)
x **= 3
print("x **= 3:", x)
x //= 2
print("x //= 2", x)



#EJERCICIO 5

# "A QUIEN MADRUGA, DIOS LE AYUDA"

refran = "A quien madruga, dios le ayuda"
print(refran.upper())               #TODO EN MAYUSCULAS
print(refran.lower())               #todo en minusculas
print(refran.title())               # Iniciales En Mayuscula    
print(refran.split())               # CREA UNA LISTA POR SUS ESPACIOS EN DIFERENTES STRING
print(refran.replace(",",";"))      # Sustituye , por ;
print(refran.replace("a",""))       # Sustituye a por espacios, o sea que las elimina



# EJERCICIO 6

puntuacion = 6
nombre_equipo = "Barcelona Futbol"
promedio_tiempo:float = 4.5
es_habil:bool = True                                                   # True si eres diestro; False si zurdo
lista_compras = ["salmon", "pollo", "jamon york", "naranja", "pan"]    # Variable tipo TUPLE
tupla_mascotas:tuple = (("Simba", 2, "gato"), ("Tobi", 3, "perro"))
dict_contactos = {"amigas": ["Lola Sanchez", "Maria Ferrer"], "telefono": [677456111,655432213],"email": ["lolasanchez@gmail.com", "mariaferrer@gmail.com"]}
lista_actividades = []                                                 # Creamos la lista vacia y vamos añadiendo 
lista_actividades.append(puntuacion)                                   # Con APPEND le añadimos las variables
lista_actividades.append(nombre_equipo)
lista_actividades.append(promedio_tiempo)
lista_actividades.append(es_habil)
lista_actividades.append(lista_compras)
lista_actividades.append(tupla_mascotas)
lista_actividades.append(dict_contactos)


#Como hacemos para saber si un elemento ya esta en la lista antes de agregarlo para evitar DUPLICARLO --> FOR IN
actividades = puntuacion, nombre_equipo, promedio_tiempo, es_habil, lista_compras, dict_contactos
lista_actividades_updated = []
for actividades in actividades:
    lista_actividades_updated.append(actividades)
    print(lista_actividades_updated)



#EJERCICIO 6.2

agenda = {
    "Ana": "654123987",
    "Luis": "678555111",
    "Marta": "622444333"
}

# 1. Mostrar todas las claves y los valores
print("Claves:", agenda.keys())
print("Valores:", agenda.values())

# 2. .get() para obtener el número de Luis y buscar a Pedro
print("Número de Luis:", agenda.get("Luis"))
print("Número de Pedro:", agenda.get("Pedro"))  # Devuelve NONE porque Pedro no está

# 3. Añadir un nuevo contacto 'Pedro'
agenda.update({"Pedro": "699876564"})
print("Agenda después de añadir a Pedro:", agenda)

# 4. Mostrar todos los pares nombre-teléfono con .items()
print("Elementos:", agenda.items())

# 5. Usar .pop() para borrar a Marta
eliminados = [agenda.pop("Marta")]
print("Agenda después de borrar a Marta:", agenda)
print(eliminados)

# 6. Limpiar la agenda con .clear()
agenda.clear()
print("Agenda vacía:", agenda)


#EJERCICIO 7

peliculas = ["Up", "El Diario de Noa", "Antes de Ti"]
print(peliculas)
peliculas.insert(3, "El Padrino")
print(peliculas)
peliculas.insert(2, "Memento")
print(peliculas)
peliculas.pop(3)    #Para mi Gladiator era posicion 3 "Antes de Ti"
print(peliculas)
peliculas.pop(2)    #Eliminamos El Padrino que es la ultima pelicula
print(peliculas)

#Si se puede eliminar con el método del numero para referirnos a la posicion en la lista

peliculas.sort()    #ORDENAR ALFABETICAMENTE
print(peliculas)
peliculas.clear     #VACIAR
print(peliculas)


#EJERCICIO 8

nota = 82

if nota >= 90:
    print("Excelente")
else:
    if nota >= 70:
        print("Bueno")
    else:
        if nota >= 50:
            print("Suficiente")
        else:
            print("Insuficiente")





