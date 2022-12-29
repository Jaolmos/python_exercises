class Monitor:
    contador_monitores = 0
    
    def __init__(self, marca, size):
        Monitor.contador_monitores +=1
        self._id_monitor = Monitor.contador_monitores
        self._marca = marca
        self._size = size

    def __str__(self):
        return f'Id: {self._id_monitor}, Marca: {self._marca}, Tamaño: {self._size}'


if __name__ == '__main__':
    monitor1 = Monitor('Acer', 22)
    print(monitor1)

    monitor2 = Monitor('Hp', 21)
    print(monitor2)