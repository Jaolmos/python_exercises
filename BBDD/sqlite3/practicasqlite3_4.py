#En este ejemplo trabajamos con la PRIMARY KEY autoincrementada
import sqlite3 

miConexion = sqlite3.connect("GestionProductos2")

miCursor = miConexion.cursor()


miCursor.execute('''

    CREATE TABLE PRODUCTOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER, 
    SECCION VARCHAR(30))
    
''')

productos = [

    ("pelota", 20, "juguetería"),
    ("pantalón", 20, "juguetería"),
    ("destornillador", 30, "juguetería"),
    ("jarrón", 50, "juguetería")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)



miConexion.commit()


miConexion.close()