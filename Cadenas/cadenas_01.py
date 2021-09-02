'''Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprime por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.'''

nombre = input('¿Cual es tu nombre: ')
numero = int(input('¿Dime un numero entero?: '))

print((nombre + '\n') * numero)