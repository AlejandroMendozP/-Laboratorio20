import numpy as np
import math

lista = np.array([10, 20, 30])

def calcular_norma(lista):
    return math.sqrt(np.sum(lista ** 2))


def normalizar(lista, modo):

    minimo = lista.min()
    maximo = lista.max()
    media = lista.mean()
    desviacion_calculo = lista.std()
    norma = calcular_norma(lista)

    try:
        match modo:
            case "minmax":
                return (lista - minimo) / (maximo - minimo)

            case "zscore":
                return (lista - media) / desviacion_calculo

            case "unit":
                if norma == 0:
                    raise ZeroDivisionError("norma = 0")
                return lista / norma

    except ZeroDivisionError as e:
        print("Error:", e)


continuar = True
while continuar:
    modo = input("Ingrese una opcion de modo o 'S' para salir: ")
    if modo.lower() == "s":
        continuar = False
        print("Saliendo")
    else:
        while (modo.lower() != "minmax" and modo.lower() != "zscore" and modo.lower() != "unit"):
            print("Opción no válida")
            modo = input("Ingrese una opcion de modo: ")
        print(normalizar(lista, modo.lower()))