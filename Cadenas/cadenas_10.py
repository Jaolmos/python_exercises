'''
Toma el siguiente código en Python que almacena una cadena:

cadena = 'X-DSPAM-Confidence:0.8475'

Utiliza 'find' y una parte de la cadena para extraer la porción de la cadena después del carácter 
puntos y después utiliza la función float para convertir la cadena extraída en un número de punto flotante.

'''

cadena = 'X-DSPAM-Confidence:0.8475'
dospuntospos = cadena.find(':') #Encuentra el carácter ":"
numero = cadena[dospuntospos + 1:] #Saca la cadena despues de los dos puntos
numero_total = float(numero)  #Convierte la cadena restante en numero flotante
print(numero_total)

