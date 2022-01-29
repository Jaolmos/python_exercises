#Juego de piedra papel y tijera

import random


def play():
    user = input("Escoge una opción: 'piedra', 'papel', 'tijera': ")
    pc = random.choice(['piedra', 'papel', 'tijera'])

    if user == pc:
        return 'Empate!!'

    if player_wins(user, pc):
        return '¡¡¡Ganaste el juego!!'

    return "¡¡¡Perdiste el juego!!!"


def player_wins(player, opponent):
    if ((player == 'piedra' and opponent == 'tijera)')
        or (player == 'papel' and opponent == 'piedra')
            or (player == 'tijera' and opponent == 'papel')):
        return True
    else:
        return False


print(play())
