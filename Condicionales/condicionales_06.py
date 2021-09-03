'''Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado
por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.'''

nombre = input("Introduce tu nombre: ")
sexo = input("¿Cual es tu sexo?(H o M)?: ")

#if sexo == "M":
    #if nombre.lower() < "m":
        #grupo = "A"
    #else:
        #grupo = "B"

#else:
    #if nombre.lower() > "n":
    #else:
        #grupo = "B"

if (nombre.lower() <"m" and sexo == "M") or (nombre.lower() >"n" and sexo == "H"):
    grupo = "A"
else:
    grupo = "B"

print("Tu grupo es el", grupo)