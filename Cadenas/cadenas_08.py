'''Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás 
hasta el primer carácter en la cadena, imprimiendo cada letra en una límea independiente.'''

palabra = 'destornillador'
indice = len(palabra) -1
while indice >= 0:
    letra = palabra[indice]
    print(letra)
    indice -=1