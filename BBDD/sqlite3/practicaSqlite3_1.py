#Insertamos productos en listas y tuplas

import sqlite3

#Creamos/abrimos la conexion.
miConexion = sqlite3.connect("BaseDatos1")

#Creamos el puntero/cursor
miCursor = miConexion.cursor()

#Ejecutamos sentencias SQL
miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(60), PRECIO INTEGER, SECCION VARCHAR(30))")

variosProductos = [
        
        ("camiseta", 15, "Deportes"),
        ("Jarrón", 90, "Cerámica"),
        ("Camión", 20, "Juguetería")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)

#Confirmamos los cambios
miConexion.commit()




#Cerramos la conexion de la base de datos.
miConexion.close()




