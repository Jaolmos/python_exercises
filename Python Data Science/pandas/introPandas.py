import pandas as pd
import numpy as np 

# Serie de datos
etiquetas = ['a','b','c','d','e','f']
datos = np.arange(4,10)
serie = pd.Series(datos, index=etiquetas)
print(serie)

# Acceder a un valor de la serie
print(serie['d'])

# Datos de distinto tipo
datos = ['Maria', 43, 'Alberto', 39]
serie = pd.Series(datos)
print(serie )

# Datos directos
serie = pd.Series([2000, 400, 3333, 600], index = ['Num01', 'Num02', 'Num03', 'Num04'])
print(serie )

# Operaciones de suma
serie1 = pd.Series([2000, 400, 3333, 600], index = ['Num01', 'Num02', 'Num03', 'Num04'])
print(serie1)

serie2 = pd.Series([1220, 300, 800, 34], index = ['Num01', 'Num02', 'Num03', 'Num04'])
print(serie2)

serie3 = serie1 + serie2
print(serie3)

# Dataframes
filas = ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columnas = ['articulo1', 'articulo2', 'articulo3']
datos = [[200, 120, 200], [300, 140, 300], [455, 122, 400], [300, 180, 520]]

dataframe = pd.DataFrame(datos, index=filas, columns=columnas)
print(dataframe)

# Seleccionar fila
print(dataframe.loc['tienda3'])

print(dataframe.loc[['tienda2','tienda3']])

# Seleccionar columnas
print(dataframe['articulo2'])

# Valor concreto
print(dataframe.loc['tienda2', 'articulo3'])

# Nueva columna
dataframe['articulo4'] = 120
print(dataframe)
dataframe['total'] = dataframe['articulo1']+dataframe['articulo2']+dataframe['articulo3']+dataframe['articulo4']
print(dataframe)

# Eliminar Columnas
print(dataframe.drop(['total'], axis=1))
print(dataframe)

#condiciones a visualizar
condicion = dataframe > 200
print(dataframe[condicion])
condicion = (dataframe['articulo1'] >= 200) & (dataframe['articulo2'] >= 100)
print(dataframe[condicion])

#Introducimos una nueva columna
nuevaColumna = '1 2 3 4'.split()
dataframe['indices'] = nuevaColumna
print(dataframe)

#Ponemos la columna 'indices' la primera
dataframe = dataframe.set_index('indices')
print(dataframe)
