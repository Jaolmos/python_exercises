#Recuperamos informacion de la base de datos

import sqlite3

#Creamos/abrimos la conexion.
miConexion = sqlite3.connect("BaseDatos1")

#Creamos el puntero/cursor
miCursor = miConexion.cursor()

#Ejecutamos sentencias SQL
#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(60), PRECIO INTEGER, SECCION VARCHAR(30))")

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall() #Nos devuelve una lista con todos los regtistros
print(variosProductos)

for producto in variosProductos:
    print(producto)
    print(producto[1])

for producto in variosProductos:
    
    print(producto[1])

#Confirmamos los cambios
miConexion.commit()




#Cerramos la conexion de la base de datos.
miConexion.close()




