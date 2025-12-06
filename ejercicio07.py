lista_estudiantes = []

def agregar_estudiante():
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    promedio = float(input("Ingrese su promedio: "))
    estudiante = {
        "nombre": nombre,
        "edad": edad,
        "promedio": promedio
    }
    lista_estudiantes.append(estudiante)

def mostrar_estudiantes():
    for estudiante in lista_estudiantes:
        print(estudiante)

def mejor_promedio():
    mayor = lista_estudiantes[0]["promedio"]
    mejor = lista_estudiantes[0]
    for i in range(len(lista_estudiantes)):
        if (lista_estudiantes[i]["promedio"] > mayor):
            mayor = lista_estudiantes[i]["promedio"]
            mejor = lista_estudiantes[i]
    print(f"El estudiante con mayor promedio es {mejor["nombre"]}")

def buscar_estudiante(nombre):
    for i in range(len(lista_estudiantes)):
        if (nombre == lista_estudiantes[i]["nombre"]):
            return lista_estudiantes[i]
    print("Estudiante no encontrado")

def eliminar_estudiante(nombre):
    for i in range(len(lista_estudiantes)):
        if (nombre == lista_estudiantes[i]["nombre"]):
            del lista_estudiantes[i]
            return
    print("Estudiante no encontrado")

while True:
    print("----- Menú -----")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Estudiante con mejor promedio")
    print("4. Buscar por nombre")
    print("5. Eliminar por nombre")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        mejor_promedio()
    elif opcion == "4":
        nombre = input("Ingrese su nombre: ")
        print(buscar_estudiante(nombre))
    elif opcion == "5":
        nombre = input("Ingrese su nombre: ")
        eliminar_estudiante(nombre)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.\n")