import funciones
import constantes

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
        matriz_jugadores = funciones.cargar_datos_jugadores(jugadores)
    elif opciones == 2:
        if matriz_jugadores == None:
            print("Error, aún no se han cargado los datos de los jugadores, seleccione la opción 1 por favor.")
        else:
            funciones.mostrar_matriz(matriz_jugadores)
    elif opciones == 3:
        if matriz_jugadores == None:
            print("Error, aún no se han cargado los datos de los jugadores, seleccione la opción 1 por favor.")
        else:
            funciones.modificar_matriz(matriz_jugadores)
print(f"*---Saliendo del menú---*")
