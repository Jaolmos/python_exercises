#Escribe un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(1,11):
    for n in range(1,11):
        print(i*n,end="\t")
    print("")