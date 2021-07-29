'''Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el Ã­ndice de masa corporal y lo almacene en una variable, y 
muestre por pantalla la frase Tu Ã­ndice de masa corporal es <imc> donde <imc> es el 
Indicee de masa corporal calculado redondeado con dos decimales.
formula: peso (kg) / [estatura (m)]2 '''

peso = float(input("¿Cuantos kilos pesas?: "))
altura = float(input("¿Cuanto mides?(en metros): "))

imc = round((peso) / (altura)**2,2)

print("Tu indice de masa corporal es", imc)