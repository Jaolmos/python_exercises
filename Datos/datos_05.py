'''Escribir un programa que pida al usuario dos números enteros y
muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde
 <n> y <m> son los números introducidos por el usuario, y <c> y <r>
son el cociente y el resto de la división entera respectivamente.'''

n = int(input('introduce el dividendo :'))
m = int(input('introduce el divisor: '))

print(n, 'entre', m, 'da un cociente', (int(n/m)), 'y un resto', (int(n % m)) )