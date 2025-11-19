# EJERCICIO 1

def convertir_a_numero(cadena):
    if cadena.isdigit():
        return int(cadena)
    else:
        print(f"❌ Mensaje de error: '{cadena}' no es válido")
        return None

print(convertir_a_numero("324"))    # 324 no da error
print(convertir_a_numero("elena"))  # Error y None
print(convertir_a_numero("32.5"))  
print(convertir_a_numero("-980"))   


# O TAMBIEN CON TRY/EXCEPT

def convertir_a_numero(valor):
    try:
        numero = int(valor)  
        print(f"Conversión exitosa: {numero}")
        return numero
    except ValueError:
        print("❌ Mensaje de error: el valor proporcionado no se puede convertir en número")


print(convertir_a_numero("324"))   
print(convertir_a_numero("elena"))  
print(convertir_a_numero("32.5"))  
print(convertir_a_numero("-980"))   





# EJERCICIO 2

def calcular_promedio(listanumeros):
    if len(listanumeros) == 0:                     # Si la lista está vacía, len(numeros) es 0 y no podemos dividir por cero
        print("No se puede calcular el promedio ya que la lista está vacia")
        return None
    suma = sum(listanumeros)
    return suma / len(listanumeros)                # La media aritmética se calcula sumando todos los elementos y dividiendo entre la cantidad de elementos

print(calcular_promedio([23, 27, 29])) 
print(calcular_promedio([]))




# EJERCICIO 3

def restar_numeros_pares(*args):    # Podemos pasarle tantos numeros como queramos
    total=50                        # Variable predefinida
    for n in args:                  # Bucle
        if n % 2 == 0:              # Numero par
            total -= n
    return total

print(restar_numeros_pares(6,12,13,16,17,19,20))




# EJERCICIO 4

def imprimir_perfil(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

perfil = {"nombre": "Elena", "edad": 23}
imprimir_perfil(**perfil)




# EJERCICIO 5

def mostrar_detalles(*detalle1, **detalle2):       # ARG POSICIONAL(*) Y ARG CON NOMBRE(**)
    for clave, valor in detalle2.items():
        print(f"Propiedades especificas: {clave} : {valor}")
    for detalle in detalle1:
        print(f"Detalles generales: {detalle}")
        print(type(detalle2))
        print(type(detalle1))

mostrar_detalles("ordenador", "apple", color='negro', forma='redonda')

# los argumentos posicionales (los que van a *args) siempre deben ir ANTES 
# de los argumentos con nombre (los que van a **kwargs)




# EJERCICIO 6

def venta_online(pedido, fecha_entrega, incidencia=False):
    if incidencia: 
        print(f"Contacte con Att.Cliente")
    else:
        print("Su pedido", pedido, "se entregará el", fecha_entrega)

venta_online("287ARf76gtH", "12-08-2023")
venta_online("287ARf76gtH", "12-08-2023", incidencia=True)
venta_online("287ARf76gtH", "12-08-2023", incidencia=False)




# EJERCICIO 7

ciudad = input("Ingresar ciudad: ")
pais = input("Ingresar pais: ")

if ciudad == pais:
    print("Son iguales")
else:
    print("No son iguales")




# EJERCICIO 8


ciudad = input("Ingresar ciudad: ")
pais = input("Ingresar pais: ")
continente = input("Ingresar continente: ")

if ciudad == pais == continente:
    print("Todos son iguales")
elif (ciudad == pais) or (ciudad == continente) or (pais == continente):
    print("Por lo menos dos son iguales")
else:
    print("No hay ninguno igual")




# EJERCICIO 9

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))

if numero1+numero2 == 10:
    print((numero1+numero2), "Es igual a 10")
elif numero1+numero2 > 10:
    print((numero1+numero2), "Es superior a 10")
elif numero1+numero2 < 10:
    print((numero1+numero2), "Es inferior a 10")




# EJERCICIO 10

listanumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in listanumeros:
    total += n
    print(f"Suma {n}, acumulada = {total}")
    if total > 100:
        print("Limite superado")
        break





# EJERCICIO 11

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for n in list1:
    if n > 150:                  # PONEMOS ESTE PRIMERO PARA QUE NOS HAGA EL BREAK EN CASO DE LLEGAR A 150, SI LO PONEMOS DEBAJO SALDRIA EL 180
        break
    if n % 5 == 0:
        print(n)



# EJERCICIO 12

precio = float(input("Ingresar precio: "))
decimales = int(input("¿Cuántos decimales quieres mostrar?: "))

redondear_precio = round(precio, decimales)

print("El precio redondeado es:", redondear_precio)      # IMPORTANTE SIEMPRE LA COMA ANTES



