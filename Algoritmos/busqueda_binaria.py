#Búsqueda binaria de un elemento en una lista de números

def busqueda_binaria(lista,valor):
    primero = 0
    ultimo = len(lista) -1

    while primero <= ultimo:
        medio = (primero+ultimo) // 2

        if lista[medio] == valor:
            return medio             #Retorna la posición del indice si encuentra el número

        else:
            if valor < lista[medio]:
                ultimo = medio - 1
            else:
                primero = medio + 1
    return None

mi_lista = [1,3,5,9,11,13,15,17,19,21]

print(busqueda_binaria(mi_lista,11))