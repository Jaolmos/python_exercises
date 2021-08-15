#8.4
'''
Escribe un programa que abra un archivo de texto y lo lea línea por linea. Cada línea dividirla en una lista de
palabras utilizando la función 'split'. Revisar si cada palabra se encuentra ya en la lista. Si la palabra no está
en la lista, agregarla a la lista. Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden
alfabético
'''

lista1 = []
archivo = open('romeo.txt')
for linea in archivo:
    palabras = linea.split() #divide la linea por palabras
    for palabra in palabras:
        if palabra in lista1:
            continue #descarta si la palbra está duplicada
        lista1.append(palabra) #Va actualizando la lista
print(sorted(lista1)) #Palabras en orden alfabético
