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
