'''
Escribe una función llamada "recortar" que tome una lista y la modifique, removiendo el primer y el último elemento, 
regresa None. Después escribe una función llamada "medio" que tome una lista y regrese una nueva lista que contenga
todo excepto el primer y el último elemento.
'''

def recortar(lst):
    del lst[0]  #Elimina el primer elemento de la lista
    del lst[-1] #Elimina el ultimo elemento de la lista

def medio(lst):
    nueva = lst[1:] #Almacena todos menos el primer elemento.
    del nueva[-1] #Elimina el último elemento.
    return nueva
lista1 = [2,4,6,8,10,12]
lista2 = [1,3,7,9,11,13]

lista_recortar = recortar(lista1)
print(lista1)
print(lista_recortar)

lista_medio = medio(lista2)
print(lista2)
print(lista_medio)