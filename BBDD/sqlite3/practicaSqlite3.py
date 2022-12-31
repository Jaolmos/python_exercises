import sqlite3

#Creamos/abrimos la conexion.
miConexion = sqlite3.connect("BaseDatos1")

#Creamos el puntero/cursor
miCursor = miConexion.cursor()

#Ejecutamos sentencias SQL
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(60), PRECIO INTEGER, SECCION VARCHAR(30))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES ('PATINES', 160, 'DEPORTES')")

#Confirmamos los cambios
miConexion.commit()




#Cerramos la conexion de la base de datos.
miConexion.close()




