# Hacemos el tablero que sea 3x3
tablero = ['-','-','-','-','-','-','-','-','-']

# Mostramos el tablero en el formato del gato
def dis():
    print('|' + tablero[0] + '|' + tablero[1] + '|' + tablero[2])
    print('|' + tablero[3] + '|' + tablero[4] + '|' + tablero[5])
    print('|' + tablero[6] + '|' + tablero[7] + '|' + tablero[8])
 
# Revisa si algún jugador ganó el juego
def revisar(tablero):
    p1 = 'x'
    p2 = 'o'
    
    # Revisa todas las probabilidades de que algun jugador haya ganado
    if tablero[0] == tablero[1] == tablero[2] == p1 or tablero[0] == tablero[1] == tablero[2] == p2:
        return True
    elif tablero[3] == tablero[4] == tablero[5] == p1 or tablero[3] == tablero[4] == tablero[5] == p2:
        return True
    elif tablero[6] == tablero[7] == tablero[8] == p1 or tablero[6] == tablero[7] == tablero[8] == p2:
        return True
    elif tablero[3] == tablero[0] == tablero[6] == p1 or tablero[3] == tablero[0] == tablero[6] == p2:
        return True
    elif tablero[1] == tablero[4] == tablero[7] == p1 or tablero[1] == tablero[4] == tablero[7] == p2:
        return True
    elif tablero[2] == tablero[5] == tablero[8] == p1 or tablero[2] == tablero[5] == tablero[8] == p2:
        return True
    elif tablero[0] == tablero[4] == tablero[8] == p1 or tablero[0] == tablero[4] == tablero[8] == p2:
        return True
    elif tablero[2] == tablero[4] == tablero[6] == p1 or tablero[2] == tablero[4] == tablero[6] == p2:
        return True
    else:
        return False

# Pregunta por la posición
def inp(tablero):
    x = int(input('Ingresa la posición: '))
    if tablero[x-1] == '-':
        return x
    else:
        print('El valor ya existe, ingrese un nuevo valor')
        return inp(tablero)
    
# Pregunta por los nombres de los jugadores
player1 = input('Nombre de jugador 1: ')
player2 = input('Nombre de jugador 2: ')
dis()

# Da los turnos para jugar
for i in range(9):     # 9 es el número de turnos máximos que puede haber
    if i%2 == 0:
        x = inp(tablero)
        tablero[x-1] = 'x'
        dis()
        if revisar(tablero):
            print('Jugador 1 gana')
            break
        else:
            x = inp(tablero)
            tablero[x-1] = 'o'
            dis()
            if revisar(tablero):
                print('Jugador 2 gana')
                break
print('Juego terminado')
