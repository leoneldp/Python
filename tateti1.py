# -*- coding: utf-8 -*-

# Elijen nombres jugadores y chequeamos que sean caracteres alfabéticos:
while True:
    name_user1 = input("Escoja el nombre del Jugador1: ")
    if name_user1.isalpha() == True:
        break

while True:
    name_user2 = input("Escoja el nombre del Jugador2: ")
    if name_user2.isalpha() == True:
        break

tablero = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
print("Tablero")
for fila in range(3):
    print("|" + "|".join(tablero[fila]) + "|")
print("")

# Jugador1 elije ficha:
while True:
    ficha_user1 = input(str(name_user1) + ", escoja el símbolo O o X: ")
    if ficha_user1 == "X" or ficha_user1 == "O":
        break
# Determina qué jugador juega primero:
if ficha_user1 == "X":
    ficha_user2= "O"
    primero=1
else:
    ficha_user2 = "X"
    primero=2


print("usuario1:", ficha_user1)
print("usuario2:", ficha_user2)
print("empieza usuario", primero)

cantJugadas = 0

def ocupadoNew(moveRow, moveCol, ficha):
    # Si está libre el casillero, ponemos X u O según jugador:
    if tablero[int(moveRow)-1][int(moveCol)-1] == "_":
        tablero[int(moveRow)-1][int(moveCol)-1] = ficha
        for fila in range(3):
            print("|" + "|".join(tablero[fila]) + "|")
        print("")
        return False
    else:
        print("Ya está ocupado")
        return True


def movement(usuario):
    """Realiza la jugada de un usuario

    Parameters:
    argument1 (int): Número de jugador que va a jugar

    Returns:
    int: Número de jugador
    
    Le pregunta al usuario las coordenadas de la jugada,
    y si está libre el casillero, ubica una X u O según
    corresponda. Imprime el tablero.
    """
    moveRow = 0
    moveCol = 0
    global cantJugadas

    if usuario == 1:
        nombre_usuario = str(name_user1)
        ficha = ficha_user1
    elif usuario==2:
        nombre_usuario = str(name_user2)
        ficha = ficha_user2

    esta_ocupado = True
    while esta_ocupado == True:
        while True:
            moveRow = input(nombre_usuario + ", escoja la fila en donde ubicará la próxima ficha. Del 1 al 3: ")
            if moveRow.isdigit()== True:
                if int(moveRow) >= 1 and int(moveRow) <= 3:
                    break
            
        while True:
            moveCol = input(nombre_usuario + ", escoja la columna en donde ubicará la próxima ficha. Del 1 al 3: ")
            if moveCol.isdigit()== True:
                if int(moveCol) >= 1 and int(moveCol) <= 3:
                    break
        
        esta_ocupado = ocupadoNew(moveRow, moveCol, ficha)

    cantJugadas += 1
    #return



def movement1(usuario):
    """Pregunta fila y columna de la jugada de un usuario

    Parameters:
    argument1 (int): Número de jugador que va a jugar

    Returns:
    int: Número de jugador
    """
    moveRow = 0
    moveCol = 0

    if usuario == 1:
        nombre_usuario = str(name_user1)
    elif usuario==2:
        nombre_usuario = str(name_user2)

    while True:
        moveRow = input(nombre_usuario + ", escoja la fila en donde ubicará la próxima ficha. Del 1 al 3: ")
        if moveRow.isdigit()== True:
            if int(moveRow) >= 1 and int(moveRow) <= 3:
                break
        
    while True:
        moveCol = input(nombre_usuario + ", escoja la columna en donde ubicará la próxima ficha. Del 1 al 3: ")
        if moveCol.isdigit()== True:
            if int(moveCol) >= 1 and int(moveCol) <= 3:
                break
    return [int(moveRow), int(moveCol)]

def ocupado(jugada, usuario):
    global cantJugadas
    if usuario == 1:
        ficha = ficha_user1
    elif usuario==2:
        ficha = ficha_user2

    # Si está libre el casillero, ponemos X u O según jugador:
    if tablero[jugada[0]-1][jugada[1]-1] == "_":
        tablero[jugada[0]-1][jugada[1]-1] = ficha
        for fila in range(3):
            print("|" + "|".join(tablero[fila]) + "|")
        print("")
    else:
        print("Ya está ocupado")
        return False
    cantJugadas += 1

def check_winner():
    """Determina si alguien ganó la partida

    Returns:
    bool: True si hay ganador
    bool: False si no lo hay
    """
    print("Cantidad Jugadas:", cantJugadas, "\n")
    if cantJugadas < 3:
        return False
    else:
        for fila in range(3):
            if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] and not tablero[fila][0] == "_":
                    print("Ganador:", tablero[fila][0], "fila:", fila)
                    return True
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and not tablero[0][col] == "_":
                    print("Ganador:", tablero[0][col], "columna:", col)
                    return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and not tablero[1][1] == "_":
            print("Ganador:", tablero[1][1], "diagonal decreciente")
            return True
        elif tablero[0][2] == tablero[1][1] == tablero[2][0] and not tablero[1][1] == "_":
            print("Ganador:", tablero[1][1], "diagonal creciente")
            return True 
        else:
            return False

# Definimos el segundo jugador:
if primero == 1:
    segundo = 2
else:
    segundo = 1

ganador = False
while ganador == False:
    movement(primero)
    #ocupado(jugada, primero)
    #ganador = check_winner()
    
    movement(segundo)
    #ocupado(jugada, segundo)
    #ganador = check_winner()
    
