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
# Determina cuál jugador juega primero y cuál segundo:
if ficha_user1 == "X":
    ficha_user2= "O"
    primero=1
    segundo=2
else:
    ficha_user2 = "X"
    primero=2
    segundo=1

cantJugadas = 0
nombre_usuario = ""

def ubica(moveRow, moveCol, ficha, nombre_usuario):
    """Ubica la ficha en el casillero

    Parameters:
    moveRow (int): Fila en la que ubicará la ficha.
    moveCol (int): Columna en la que ubicará la ficha.
    ficha (str): X u O, la ficha del usuario que juega.
    nombre_usuario (str): nombre del usuario que juega.

    Si está libre el casillero, ubica la ficha X u O y devuelve False
    Si está ocupado, devuelve True.
    """    
    if tablero[int(moveRow)-1][int(moveCol)-1] == "_":
        tablero[int(moveRow)-1][int(moveCol)-1] = ficha
        for fila in range(3):
            print("|" + "|".join(tablero[fila]) + "|")
        print("")
        return False
    else:
        print(nombre_usuario, "el casillero que eligió ya está ocupado, elija otro por favor.")
        return True

def movement(usuario):
    """Realiza la jugada de un usuario

    Parameters:
    usuario (int): Número de jugador que va a jugar

    Le pregunta al usuario las coordenadas de la jugada,
    y si está libre el casillero, ubica una X u O según
    corresponda. Imprime el tablero.
    """
    moveRow = 0
    moveCol = 0
    global cantJugadas
    global nombre_usuario

    if usuario == 1:
        nombre_usuario = str(name_user1)
        ficha = ficha_user1
    elif usuario==2:
        nombre_usuario = str(name_user2)
        ficha = ficha_user2

    esta_ocupado = True
    while esta_ocupado == True:
        while True:
            moveRow = input(nombre_usuario + " escoja la fila en donde ubicará la próxima ficha. Del 1 al 3: ")
            if moveRow.isdigit()== True:
                if int(moveRow) >= 1 and int(moveRow) <= 3:
                    break
            
        while True:
            moveCol = input(nombre_usuario + " escoja la columna en donde ubicará la próxima ficha. Del 1 al 3: ")
            if moveCol.isdigit()== True:
                if int(moveCol) >= 1 and int(moveCol) <= 3:
                    break
        
        esta_ocupado = ubica(moveRow, moveCol, ficha, nombre_usuario)

    cantJugadas += 1

def check_winner():
    """Determina si alguien ganó la partida

    Returns:
    bool: True si hay ganador
    bool: False si no lo hay

    Chequea si alguna fila o columna tiene todas X o todas O
    Chequea si alguna diagonal tiene todas X o todas O
    En caso afirmativo: felicita al usuario y devuelve True
    En caso negativo: devuelve False
    """
    print()
    if cantJugadas < 3:
        return False
    else:
        for fila in range(3):
            if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] and not tablero[fila][0] == "_":
                    print("¡Felicitaciones "+ nombre_usuario+ ", ha ganado!")
                    return True
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and not tablero[0][col] == "_":
                    print("¡Felicitaciones "+ nombre_usuario+ ", ha ganado!")
                    return True
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and not tablero[1][1] == "_":
            print("¡Felicitaciones "+ nombre_usuario+ ", ha ganado!")
            return True
        elif tablero[0][2] == tablero[1][1] == tablero[2][0] and not tablero[1][1] == "_":
            print("¡Felicitaciones "+ nombre_usuario+ ", ha ganado!")
            return True
        else:
            return False

# Ejecutamos los movimientos y determinamos si hay ganador:
while True:
    movement(primero)
    ganador = check_winner()
    if ganador == True:
        break
    
    movement(segundo)
    ganador = check_winner()
    if ganador == True:
        break

