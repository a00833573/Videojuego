from collection import deque

turno = deque(["1","2"])
tablero = [ [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def rotar_turno():
    turno.rotate()
    return turno[0]

def mostrar_tablero():
    print ("")
    for fila in tablero:
        print (fila)

def juego():
    mostrar_tablero()
    jugador = rotar_turno()
    while True:
        input("Turno de jugador {}. Elije la posición fila,columna de 1 a 3".format(jugador))
        if posicion == 'Salir':
            break
        jugador = rotar_turno()
        
juego()
#continuamos
