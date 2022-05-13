from collection import deque

turno = deque(["1","2"])
tablero = [ [" ", " ", " "], 
           [" ", " ", " "], 
           [" ", " ", " "]]

def rotar_turno():
    turno.rotate()
    return turno[0]

def mostrar_tablero():
    print ("")
    for fila in tablero:
        print (fila)
        
def procesar_posicion(posicion):
    fila,columna=posicion.split(',')
    return [int(fila)-1,int(columna)-1]

def posicion_correcta(posicion):
    if 0 <= posicion[0] <= 2 and 0 <= posicion[1] <= posicion:
        if tablero[posicion[0]][posicion[1]] == "":
            return True
    return False

def

def juego():
    mostrar_tablero()
    jugador = rotar_turno()
    while True:
        input("Turno de jugador {}. Elije la posición fila,columna de 1 a 3".format(jugador))
        if posicion == 'Salir':
            break
        jugador = rotar_turno()
        try:
            posicion_1 = procesar_posicion(posicion)
        except:
            print)"Error, posicion {} no es valida".format(posicion)
            continue
        if posicion_correcta(posicion_1):
            print("correcta")
            actualizar_tablero(posicion_1,jugador) 
        else:
            print("incorrecta")
        
juego()
#continuamos
