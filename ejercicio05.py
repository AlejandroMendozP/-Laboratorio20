def pedir_n():
    while True:
            n = int(input("Ingrese un número mayor a 3: "))
            if n >= 3:
                return n
            else:
                print("N debe ser mayor o igual a 3.")

def generar_espiral(n):
    matriz = [[0]*n for _ in range(n)]
    
    num = 1
    izquierda = 0
    derecha = n - 1
    arriba = 0
    abajo = n - 1

    while num <= n*n:

        for c in range(izquierda, derecha + 1):
            matriz[arriba][c] = num
            num += 1
        arriba += 1

        for f in range(arriba, abajo + 1):
            matriz[f][derecha] = num
            num += 1
        derecha -= 1

        for c in range(derecha, izquierda - 1, -1):
            matriz[abajo][c] = num
            num += 1
        abajo -= 1

        for f in range(abajo, arriba - 1, -1):
            matriz[f][izquierda] = num
            num += 1
        izquierda += 1

    return matriz

def mostrar_matriz(m):
    for fila in m:
        print(*fila)

n = pedir_n()
matriz = generar_espiral(n)
mostrar_matriz(matriz)
