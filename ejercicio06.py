import array
import math

lista = array.array('i', [10, 20, 30])

def desviacion(lista, media):
    lista = array.array('d', ((x - media) ** 2 for x in lista))
    division = sum(lista) / len(lista)
    desviacion = math.sqrt(division)
    return desviacion

def calcular_norma(lista):
    lista = array.array('d', ((x ** 2) for x in lista))
    suma = math.sqrt(sum(lista))
    return suma

def normalizar(lista, modo):

    min = lista[0]
    for i in range(len(lista)):
        if lista[i] < min:
            min = lista[i]

    max = lista[0]
    for i in range(len(lista)):
        if lista[i] > max:
            max = lista[i]

    media = sum(lista) / len(lista)
    desviacion_calculo = desviacion(lista, media)
    norma = calcular_norma(lista)

    try:
        match modo:
            case "minmax":
                lista = array.array('d', ((x - min) / (max - min) for x in lista))
                return lista
            case "zscore":
                lista = array.array('d', ((x - media) / desviacion_calculo for x in lista))
                return lista
            case "unit":
                lista = array.array('d', ((x / norma) for x in lista))
                return lista
            case _:
                print("Opción no válida")

    except ZeroDivisionError as e:
        print("Error:", e)
        return None


continuar = True

while continuar:
    modo = input("Ingrese una opción de modo o 'S' para salir: ")
    if modo.lower() == "s":
        print("Saliendo...")
        continuar = False
        break

    while modo.lower() not in ("minmax", "zscore", "unit"):
        print("Opción no válida")
        modo = input("Ingrese una opción de modo: ")

    print(normalizar(lista, modo.lower()))