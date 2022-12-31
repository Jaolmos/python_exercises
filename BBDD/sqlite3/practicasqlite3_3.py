#En este ejemplo trabajamos con la PRIMARY KEY
import sqlite3 

miConexion = sqlite3.connect("GestionProductos")

miCursor = miConexion.cursor()


miCursor.execute()

productos = [

    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalón", 20, "juguetería"),
    ("AR03", "destornillador", 30, "juguetería"),
    ("AR04", "jarrón", 50, "juguetería")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)



miConexion.commit()


miConexion.close()