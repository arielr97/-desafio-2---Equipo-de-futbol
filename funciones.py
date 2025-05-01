import constantes

def cargar_datos_jugadores(jugadores: int) -> list:
    print("-Ha seleccionado cargar datos de los jugadores, a continuación le pediremos los datos necesarios-\n")
    matriz = [[0] * 5 for k in range(jugadores)]
    for i in range(len(matriz)):
        matriz[i][0] = input(f"Ingrese el nombre del jugador {i+1}: ")
        matriz[i][1] = input(f"Ingrese el apellido del jugador {i+1}: ")
        matriz[i][2] = input(f"Ingrese la edad del jugador {i+1}: ")
        matriz[i][3] = input(f"Ingrese la posición en la que juega el jugador {i+1}: ")
        matriz[i][4] = input(f"Ingrese la cantidad de goles en el torneo que tiene el jugador {i+1}: ")
    return matriz

def mostrar_matriz(matriz: list):
    print("-Ha seleccionado ver la información de todos los jugadores-\n")
    for i in range(len(matriz)):
        print(f"#Jugador {i+1}: ")
        for j in range(len(matriz[i])):
            match j:
                case 0:
                    print(f"Nombre del jugador {i+1}: {matriz[i][j]}")
                case 1:
                    print(f"Apellido del jugador {i+1}: {matriz[i][j]}")
                case 2:
                    print(f"Edad del jugador {i+1}: {matriz[i][j]}")
                case 3:
                    print(f"Posición en la que juega el jugador {i+1}: {matriz[i][j]}")
                case _:
                    print(f"Goles que lleva en el torneo el jugador {i+1}: {matriz[i][j]}")
        print("")

def modificar_matriz(matriz: list):
    print("-Ha seleccionado modificar datos de un jugador-")
    print("-A continuación se mostrará la matriz de jugadores indicando el número de fila de cada jugador-\n")
    for i in range(len(matriz)):
        print(f"Fila {i}: {matriz[i]}")
    fila = int(input("Indique el jugador a modificar colocando a continuación el número de fila del jugador: "))
    while (fila < 0 or fila >= len(matriz)):  #validación
        fila = int(input("Error, indique un número de fila válido: "))
    columna = int(input("Indique con un número el dato del jugador a modificar (0:Nombre | 1:Apellido | 2: Edad | 3:Posición | 4:Goles en el torneo): "))
    while columna < 0 or columna >= len(matriz[0]):  #validación
        columna = int(input("Error, indique un número de dato válido (0:Nombre | 1:Apellido | 2: Edad | 3:Posición | 4:Goles en el torneo): "))
    print(f"Se modificará la siguiente fila: {matriz[fila]} en la columna {columna}:{constantes.DATOS[columna]} por el siguiente dato.")
    matriz[fila][columna] = input("Ingrese el nuevo dato: ")

def menu():
    print("*---Bienvenido al menú---*")
    print("Seleccione una de las opciones a continuación ingresando un número válido:")
    matriz_jugadores = None
    opciones = 0
    while opciones != 4:
        opciones = int(input("\n(1: Cargar datos de los jugadores | 2: Ver información de los jugadores | 3: Modificar datos de un jugador | 4: Salir): "))
        while opciones < 1 or opciones > 4:
            opciones = int(input("Error, seleccione una de las opciones válidas:\n(1: Cargar datos de los jugadores | 2: Ver información de los jugadores | 3: Modificar datos de un jugador | 4: Salir): "))
        print(f"*Seleccionó la opción: {opciones}*")
        if opciones == 1:
            jugadores = constantes.CANTIDAD_JUGADORES
            matriz_jugadores = cargar_datos_jugadores(jugadores)
        elif opciones == 2:
            if matriz_jugadores == None:
                print("Error, aún no se han cargado los datos de los jugadores, seleccione la opción 1 por favor.")
            else:
                mostrar_matriz(matriz_jugadores)
        elif opciones == 3:
            if matriz_jugadores == None:
                print("Error, aún no se han cargado los datos de los jugadores, seleccione la opción 1 por favor.")
            else:
                modificar_matriz(matriz_jugadores)
    print(f"*---Saliendo del menú---*")
    