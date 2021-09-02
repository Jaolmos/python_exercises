'''
Encapsula el código siguiente en una funciíon llamada cuenta, y hazla genérica de tal modo que pueda 
aceptar una cadena y una letra como argumentos.
'''


def cuenta(palabra,letra):  #cuenta el numero de veces que una letra aparece en una palabra determinada.

    contador = 1
    
    for caracter in palabra:
        if caracter == letra:
            contador = contador + 1
    print('La letra',entrada_letra,'se encuentra en la palabra',entrada_palabra,contador,'veces.')
            
entrada_palabra = input('Introduce una palabra: ')
entrada_letra = input('Introduce una letra:')
cuenta(entrada_palabra,entrada_letra)
