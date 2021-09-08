#Programa para ordenar un arreglo de numeros de menor a mayor.

def encuentraMenor(arreglo): #Función para encontrar el menor elemento de un arreglo.
    menor = arreglo[0]
    menor_indice = 0
    for i in range(1,len(arreglo)):
        if arreglo[i] < menor:
            menor = arreglo[i]
            menor_indice = i
    return menor_indice

def ordenacionPorSeleccion(arreglo): #Función de Ordenación por seleccion. 
    nuevaLista=[]
    for i in range(len(arreglo)):
        menor=encuentraMenor(arreglo)
        nuevaLista.append(arreglo.pop(menor))
    return nuevaLista


mi_arreglo= [166,34,12,345,444,222,1,45,33,555,2222,2,444444,12,222345,40,22]

print(ordenacionPorSeleccion(mi_arreglo))