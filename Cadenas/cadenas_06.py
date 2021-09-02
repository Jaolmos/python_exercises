'''Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.'''

frase = input("Introduce una frase: ")

vocal = input("Introduce una vocal en minuscula: ")

print(frase.replace(vocal, vocal.upper()))