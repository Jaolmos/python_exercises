'''Practicas con la libreria Numpys de Python'''



#Listas en array
import numpy as np

lista1 = [1,2,3,4,5,6,2,4,8,4,9]
array1 = np.array(lista1)

print(lista1)
print(type(array1))
print(array1)


lista2 = [[1,4,5],[3,1,7],[8,5,3]]
array2 = np.array(lista2)
print(array2)


#Arrays automaticos añadiendo el rango'''

#array = np.arange(9)

array = np.arange(2, 15, 2)
print(array)

#Generamos una matriz con ceros
matrizCeros = np.zeros((5,6))
print(matrizCeros)

#Generamos una matriz con unos
matrizUnos = np.ones((3,5))
print(matrizUnos)

#Matriz de 50 elementos con valores del 2 al 7
matriz = np.linspace(2,7,50)
print(matriz)

#Matriz identidad
matrizIdentidad = np.eye(7)
print(matrizIdentidad)

#Matriz con numeros aleatorios
matrizAleatoria = np.random.rand(3, 4)
print(matrizAleatoria)

matrizAleatoriaNormal = np.random.randn(4)
print(matrizAleatoriaNormal)

matrizAleatoriaEnteros = np.random.randint(1,51, 20)
print(matrizAleatoriaEnteros)

#Tamaño de los arrays
array = np.random.randint(1,180,30)
print(array)
matriz = array.reshape(5,6)
print(matriz)

#Maximo y minimo
array = np.random.randint(1, 800, 200)
print(array)
maximo = array.max()
print(maximo)
print(array.argmax()) #posicion del numero maximo

minimo = array.min()
print(minimo)
print(array.argmin()) #posicion del numero minimo

#Mostrar elementos
array = np.arange(1,15)
print(array)
print(array[3])
print(array[4:])
print(array[:5])

# Copiar un array
array2 = array.copy()
print(array)
print(array2)
array2[2] = 333
print(array)
print(array2)

#Operaciones con matrices
print(matriz)
print(matriz[0])
print(matriz[:2])
print(matriz[2][3]) #print(matriz[2,3]) equivalente con el mismo resultado
print(matriz)
print(matriz+10) #Se le suma 10 a cada elemento de la matriz
print(np.max(matriz))

condicion = matriz < 40 #Valores mayores de 10
print(matriz)
print(condicion)
print(matriz[condicion]) #Devuelve un array con los valores que cumplen la condicion

#Numeros impares
condicion = (matriz % 2 != 0) #Devuelve los numeros impares de la matriz
print(matriz[condicion]) 

# Practica
lista = np.arange(5,41) #Array con valores del 5 al 40
print(lista)
lista = lista.reshape(3,12) #Redimensionamos el array
print(lista)
print(lista[2,4]) #Mostramos un elemento del array

# Combinacion primitiva
arrayPrimitiva = np.random.randint(1,50,6)
print(arrayPrimitiva)


