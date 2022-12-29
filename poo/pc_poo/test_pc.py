from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


raton1 = Raton('Logitech', 'USB')
monitor1 = Monitor('Acer', 26)
teclado1 = Teclado('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)


raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('HP', 19)
teclado2 = Teclado('Acer', 'Bluetooth')
Computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

Computadoras1= [computadora1, Computadora2]
orden1 = Orden(Computadoras1)
print(orden1)