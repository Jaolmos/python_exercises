'''Escribe un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero
el programa debe mostrar un error. Redondeamos las decimales 3 cifras.'''

dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

if divisor == 0:
    print("Error!!no se puede dividir por cero!!")
else:
    division = round((dividendo/divisor),3) #redondeamos las decimales 3 cifras
    print(division)

    