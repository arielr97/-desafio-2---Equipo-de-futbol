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
        print(f"Nombre del jugador {i+1}: {matriz[i][0]}")
        print(f"Apellido del jugador {i+1}: {matriz[i][1]}")
        print(f"Edad del jugador {i+1}: {matriz[i][2]}")
        print(f"Posición en la que juega el jugador {i+1}: {matriz[i][3]}")
        print(f"Goles que lleva en el torneo el jugador {i+1}: {matriz[i][4]}")
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

    