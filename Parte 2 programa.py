
# Parte 2 programa actividad 26.py
# Representación del almacenamiento.
disco = [1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

# Registro de los archivos almacenados.
archivos = {}


def mostrar_estado():
    
    print("Estado final del disco:", disco)
    print("\nDistribución de los bloques:")
    # Mostramos el estado de cada bloque.
    for posicion, estado in enumerate(disco):

        if estado == 0:
            print("Bloque", posicion, "; Libre")
        else:
            print("Bloque", posicion, "; Ocupado")

    # Contamos los bloques disponibles.
    libres = disco.count(0)
    
    
    
    
    print("\nResumen del almacenamiento:")
    print("Bloques libres:", libres)
    print("Bloques ocupados:", disco.count(1))

# -----------------------------------------------------------------------------------------------
def almacenar_contiguo():
    # Almacenar mediante asignación contigua

    nombre_archivo = str(input("Ingrese el nombre del archivo a almacenar: "))
    necesarios = int(input("Ingrese el número de bloques necesarios para almacenarlo: "))

    if nombre_archivo in archivos:
        print("Ya existe un archivo con ese nombre.")
        return

    if necesarios <= 0:
        print("La cantidad de bloques debe ser mayor que cero.")
        return

    inicio = -1

    # Buscamos una secuencia de bloques libres.
    for i in range(len(disco) - necesarios + 1):

        disponibles = True

        for j in range(necesarios):
            if disco[i + j] != 0:
                disponibles = False
                break

        if disponibles:
            inicio = i
            break

    # Asignamos los bloques encontrados.
    if inicio != -1:
        for i in range(inicio, inicio + necesarios):
            disco[i] = 1

        print("Archivo almacenado desde el bloque", inicio)

        posiciones = list(range(inicio, inicio + necesarios))
        archivos[nombre_archivo] = posiciones

    else:
        print("No existe espacio contiguo suficiente.")
        
    

# -----------------------------------------------------------------------------------------------
def almacenar_no_contiguo():
    # Almacenar con almacenamiento no contiguo

    nombre_archivo = str(input("Ingrese el nombre del archivo a almacenar: "))
    necesarios = int(input("Ingrese la cantidad de bloques necesarios para almacenar su archivo"))

    if nombre_archivo in archivos:
        print("Ya existe un archivo con ese nombre.")
        return

    if necesarios <= 0:
        print("La cantidad de bloques debe ser mayor que cero.")
        return

    seleccionados = []

    # Buscamos bloques libres.
    for i in range(len(disco)):

        if disco[i] == 0:
            seleccionados.append(i)

        if len(seleccionados) == necesarios:
            break

    # Comprobamos si hay espacio suficiente.
    if len(seleccionados) == necesarios:

        for posicion in seleccionados:
            disco[posicion] = 1

        print("Bloques asignados:", seleccionados)

        archivos[nombre_archivo] = seleccionados

    else:

        print("Espacio insuficiente.")

# ---   


def eliminar_archivo():
    nombre_archivo = str(input("Ingrese el nombre del archivo que desea eliminar: "))

    if nombre_archivo not in archivos:
        print("El archivo no existe.")
        return

    for posicion in archivos[nombre_archivo]:
        disco[posicion] = 0

    del archivos[nombre_archivo]

    print("Archivo eliminado correctamente.")
    print("Bloques liberados.")


def consultar_archivo():
    nombre_archivo = str(input("Ingrese el nombre del archivo que desea consultar: "))

    if nombre_archivo not in archivos:
        print("El archivo no existe.")
        return

    posiciones = archivos[nombre_archivo]

    print("Nombre del archivo:", nombre_archivo)
    print("Cantidad de bloques asignados:", len(posiciones))
    print("Posiciones que ocupa:", posiciones)


# Menú
print("Bienvenido al sistema de almacenamiento documental")

opcion = 0

while opcion != 6:
    print("\nMenú principal")
    print("1. Mostrar estado del disco")
    print("2. Almacenar archivo mediante asignación contigua")
    print("3. Almacenar archivo mediante asignación no contigua")
    print("4. Eliminar un archivo")
    print("5. Consultar distribución de un archivo")
    print("6. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        mostrar_estado()

    elif opcion == 2:
        almacenar_contiguo()

    elif opcion == 3:
        almacenar_no_contiguo()

    elif opcion == 4:
        eliminar_archivo()

    elif opcion == 5:
        consultar_archivo()

    elif opcion == 6:
        print("Programa finalizado.")

    else:
        print("Opción no válida. Intente nuevamente.")
