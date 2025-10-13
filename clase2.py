# EJERCICIO 1

numeroazar = 3
numeros = [1,2,3,4]

for numero in numeros:     # Con un BUCLE, for, se recorre la lista elemento por elemento
    print(numeroazar*numero)


# EJERCICIO 2
# PARA CREAR E IMPRIMIR UNA SECUENCIA DE NUMEROS CONSECUTIVOS UTILIZAMOS RANGE 
# PYTHON LLEGA HASTA 1 ANTES DEL FINAL, EMPEZANDO POR CERO 

x = range(-10, 0)               # Empieza en 10 y termina en -1, no en 0
for n in x:                     # Si fuera (27, 87) terminaria en el 86
    print(n)                    # La n en for n in x: es simplemente una variable temporal 
                                # que usamos dentro del bucle para representar cada elemento de la secuencia

# La función range(start, stop, step) sirve para crear una secuencia de números en Python.
#start → el número donde empieza la secuencia.

#stop → el número donde termina, pero sin incluirlo.

#step → el tamaño del paso (es decir, cuánto se incrementa o decrementa cada vez).

for n in range(-10, 0, 2):
    print(n)

#start = -10, empieza en el 10
#stop = 0, se para en el 0 pero no lo imprime
#step = 2, o sea que va de dos en dos



# EJERCICIO 3
#Recorra los números del 150 al 350 (SIN incluir el 350)
#Imprima solo los que sean divisibles por 5 y por 7

for n in range (150, 350):
    if n % 5 == 0 and n % 7 == 0:              # n % 5 == 0  o n % 7 == 0→ significa que el número n es divisible por 5 / 7
        print(n)                               #El operador % (módulo) devuelve el resto de una división.
                                               #Si el resto es 0, significa que el número es divisible.




# EJERCICIO 4
# Se llama BUCLE ANIDADO, porque está uno dentro de otro

for n in range (5, 0, -1):                     # Ponemos el -1 porque vamos del 5 al 0, para atrás, BAJA
    for o in range(n, 0, -1):
        print(o, end = "")                     # Imprime los numeros en la misma linea, separados por un espacio



# EJERCICIO 5

numeros = [3, 13, 30, 33, 44, 99]            # Coleccion de numeros que vamos a recorrer

contador = 0                                 # Guardará cuantos numeros especiales cumplen la condicion

for n in numeros:
    if n % 3 == 0 or '3' in str(n):          # Si n es multiplo de 3 o si n contiene el digito '3'
        contador += 1                        # Sila condicion se cumple, sumale 1 al contador
print(f"Numeros especiales encontrados: {contador}")  



# EJERCICIO 6

def cuentaAtras (n):                    # Definimos la función
    for i in range(n, -1, -1):          # Creamos el bucle en orden descendente
        if i % 4 == 0 and i != 0:       # Si el numero es divisible por 4 y distinto a 0
            print("Pum!")              
        elif i == 0:                    # Si el numero es igual a 0. ELIF es else if pero acortado
            print("¡Despegue!")
        else:                           # Si no cumple ninguna de las otras 2
            print(i)



# EJERCICIO 7

#RECORDAMOS METODOS STRINGS: isupper(), islower(), isdigit().

frase = "Ole Python como mola! Me está encantando. De verdad que SÍ"

mayusculas = 0
minusculas = 0
digitos = 0

for f in frase: 
    if f.isupper():            # Si es letra mayuscula
        mayusculas += 1
    elif f.islower ():         # Si es letra minuscula
        minusculas += 1
    elif f.isdigit:            # Si es digito
        digitos += 1

print(f"Letras mayúsculas: {mayusculas}")
print(f"Letras minúsculas: {minusculas}")
print(f"Digitos: {digitos}")



# EJERCICIO 8

def diadelasemana (n):
    if n == 1:
        return "Lunes"
    elif n == 2:
        return "Martes"
    elif n == 3:
        return "Miercoles"
    elif n == 4:
        return "Jueves"
    elif n == 5:
        return "Viernes"
    elif n == 6:
        return "Sabado"
    elif n == 7:
        return "Domingo"
    else:
        return "No es un dia de la semana"
    
print(diadelasemana(9))
print(diadelasemana(5))




#EJERCICIO 9

def piramideInvertida (filas):
    for n in range (filas, 0, -1):         # Bucle exterior --> controla las filas
        for n in range(n, 0, -1):          # Bucle interior --> controla los numeros dentro de la fila
            print(n, end=" ")              # Evita saltos de linea para que los nums esten en la misma fila
        print()                            # Salto de linea al final de cada fila
piramideInvertida(50)




# EJERCICIO 10

def compararNumeros (numero1, numero2):
    if numero1 == numero2:
        return f'{numero1} y {numero2} son iguales'
    if numero1 > numero2:
        return f' {numero1} es mayor que {numero2}'
    if numero1 < numero2:
        return f'{numero2} es mayor a {numero1}'
    
print(compararNumeros(3,3))
print(compararNumeros(20,5))



# EJERCICIO 11

def cuentaletras (texto, letra):
    texto = texto.lower()           # Convertimos todo a minusculas para ignorar las mayusculas o minusculas
    letra = letra.lower()           # Letra minuscula
    return texto.count(letra)       # Cuantas veces aparece la letra

resultado = cuentaletras('Me gustaría trabajar en el mundo de Data', 'e')
print(resultado) 


# EJERCICIO 12

def contarLetras (texto):
    texto = texto.lower()        # Todo a minusculas
    conteo = {}                  # Diccionario vacio para almacenar el conteo 

    for letra in texto:
        if letra.isalpha():
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1
    return(conteo)


resultado = contarLetras("Me gusta el mundo de los datos")
print(resultado)


# EJERCICIO 13