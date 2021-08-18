# encoding: utf-8

lista = list() #Lista de números

def sumar(lista):
    resultado = 0
    lista.pop()
    for x in lista:
        resultado += x
    print("Suma de los siguientes números:")
    print(lista)
    return resultado

def restar(lista):
    resultado = aux = lista[0] 
    lista.pop(0)
    lista.pop()
    for x in lista:
        if x != 0:
            resultado -= x
    print("Resta de los siguientes números:")
    lista.insert(0,aux)
    print(lista)
    return resultado

def multiplicar(lista):
    resultado = 1
    lista.pop()
    for x in lista:
        if x != 0:
            resultado *= x
    print("Multiplicación de los siguientes números:")
    print(lista)
    return resultado

def dividir(lista):
    resultado = aux = lista[0] 
    lista.pop(0)
    lista.pop()
    for x in lista:
        if x != 0:
            resultado /= x
    print("División de los siguientes números:")
    lista.insert(0,aux)
    print(lista)
    return resultado

def potencia(lista):
    resultado = aux = lista[0]
    lista.pop(0)
    lista.pop()
    for x in lista:
        if x != 0:
            resultado **= x
    print("Potencia de los siguientes números:")
    print(lista)
    return resultado

def promedio(lista):
    resultado = 0
    lista.pop()
    for x in lista:
        resultado += x
    print("Promedio entre los siguientes números:")
    print(lista)
    return resultado / (len(lista))
   
def leer():
    numero = 1
    while (numero != 0):
        numero = float(raw_input("Introduce un valor numérico o '0' para finalizar: ") )
        lista.append(numero)
        print(" ")


opcion = 0

while True:
    print("""
    CALCULADORA
    
    1) Sumar  números
    2) Restar números
    3) Multiplicar números
    4) Dividir números
    5) Potencia de números
    6) Promedio de números
    7) Salir
    """)
    
    opcion = int(input("Elige una opción: "))

    if (opcion == 1):
        leer()
        print("El resultado es: ",sumar(lista))
        del lista[:]
    elif opcion == 2:
        leer()
        print("El resultado es: ",restar(lista))
        del lista[:]
    elif opcion == 3:
        leer()
        print("El resultado es: ",multiplicar(lista))
        del lista[:]
    elif opcion == 4:
        leer()
        print("El resultado es: ",dividir(lista))  
        del lista[:]
    elif opcion == 5:
        leer()
        print("El resultado es: ",potencia(lista))
        del lista[:]
    elif opcion == 6:
        leer()
        print("El resultado es: ",promedio(lista))
        del lista[:]
    elif opcion == 7:
        exit()
    else:
        print("No se ingresó una opccón válida, por favor, intente nuevamente...")
        del lista[:]

