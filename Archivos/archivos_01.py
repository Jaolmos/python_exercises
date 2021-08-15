
'''Escribe un programa que solicite un nombre de archivo de texto e imprima su contenido 
(línea por línea), todo en mayúsculas.'''

archivo_open = input('Introduce el nombre del archivo que quieres procesar: ')
try: 
    archivo = open(archivo_open)
except: 
    print('No se puede abrir el archivo: ',archivo_open)
    exit()
    
for linea in archivo:
    proceso = linea.rstrip().upper() #Borramos carácteres finales. Convertimos en mayúsculas-
    print(proceso)

    #Adjunto el archivo de texto texto.txt para procesaslo.