from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Comnputadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Comnputadora.contador_computadoras += 1
        self._id_computadora = Comnputadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Techado: {self._teclado}
        Raton: {self._raton}
        '''


if __name__ == '__main__':
    
    raton1 = Raton('Logitech', 'USB')
    monitor1 = Monitor('Acer', 26)
    teclado1 = Teclado('HP', 'USB')

    computadora1 = Comnputadora('HP', monitor1, teclado1, raton1)
    print(computadora1)