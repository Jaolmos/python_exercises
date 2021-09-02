'''Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es 
el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-22). 
Escribir un programa que pregunte por un número de teléfono con este formato en la consola y 
muestre por pantalla el número de teléfono sin el prefijo y la extensión.'''

tlf = input('Introduce un numero de telefono con el formato del ejemplo "+34-913724710-22": ')

print('Tu numero de telefono es: ', tlf[4:-3])