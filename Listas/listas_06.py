'''Escribe un programa para leer a través de los datos de una bandeja de entrada de correo y cuando encuentres
una línea que comience con "From", divide la línea en palabras utilizando la función "split".
ejemplo: From martin@media.berkeley.edu Fri Jan  4 14:10:44

Estamos interesados en quién envió el mensaje, sería la segunda palabra en las líneas que comienza con From 
(no incluir From:). Tambiém tendrás que contar el número de líneas "From" e imprimir el total al final.'''

archivo = open('inbox.txt')
contador = 0

for linea in archivo:
    palabras = linea.split()
    if  len(palabras) < 3 or palabras[0] != 'From':
        continue
    print(palabras[1])
    contador += 1

print('Hay', contador, 'lineas en el archivo "Innbox.txt" con la palabra "From" al inicio.')