'''Escribe un programa que solicite un nombre de archivo y después  lea ese archivo buscando las líneas 
que tengan la siguiente forma: X-DSPAM-Confidence: 0.6178.

Cuando encuentres una línea que comience con "X-DSPAM-Confidence" ponla a parte para extraer el número
decimal de la línea. Cuenta esas líneas y después calcula el total acumulado de los valores de 
"spam-confidence". Cuando llegues al final del archivo, imprime el valor medio de "spam confidence".'''

contador = 0
total = 0

archivo_open = input('Introduce el nombre del archivo que quieres procesar: ')
try:
    archivo = open(archivo_open)
except:
    print('No se puede abrir el archivo: ',archivo_open)
    exit()

for linea in archivo:
    if linea.startswith('X-DSPAM-Confidence: '):
        contador = contador + 1
        dospuntospos = linea.find(':')
        numero = linea[dospuntospos + 1:].strip() #Elimina todo el texto, excepto el número.
        dspam = float(numero)
        total = total + dspam

promedio = total / contador
print('Promedio spam confidence: ',promedio)

#Se adjunta el archivo de texto texto.txt para procesarlo.
