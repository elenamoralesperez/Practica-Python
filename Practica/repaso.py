# Ejercicio 1
# Crea una función que determine qué debe hacer el usuario, según la hora del día. 
# El usuario debe ingresar por consola qué hora es (la hora, no los minutos), 
# y el programa le debe decir qué está agendado a esa hora. La casuística es la siguiente:

# Si es entre las 0 y las 8, print "Durmiendo"
# Si es entre las 9 y las 18, print "Trabajando"
# Si es entre las 19 y las 21, print "Clase"
# Si es entre las 22 y las 24, print "Descanso"
# En cualquier otro caso, print "Transporte o error"
# Implementa mediante sentencias if/elif/else.

def agenda_por_hora():
    hora = int(input("¿Qué hora es? Solo en punto, no minutos: "))
    if 0 <= hora <= 8:
        print("Durmiendo")
    elif 9 <= hora <= 18:
        print("Trabajando")
    elif 19 <= hora <= 21:
        print("Clase")
    elif 22 <= hora <= 24:
        print("Descanso")
    else:
        print("Transporte o error")

agenda_por_hora()



# Ejercicio 2
# En este ejercicio vamos a implementar un calculador de precios de casas muy sencillo. Tenemos las siguientes variables:

# superficie
# distrito

# Implementa mediante sentencias if/elif/else la siguiente casuística:

# Si el distrito es "Moncloa" o "Centro", y además la superficie es superior a 100 metros cuadrados, el precio de la casa es de 1000
# Si el distrito es "Salamanca", y además la superficie de la casa es al menos de 150 metros, el precio de la casa es de 1500
# Si el distrito no es "Retiro" y la superficie está entre 60 y 80 metros, el precio es de 600
# En cualquier otro caso, el precio será de 0
# Crea la calculadora de precios mediante una función que le pida al usuario el distrito y la superficie mediante input. Utiliza los bucles y el control de flujos que consideres adecuados.
