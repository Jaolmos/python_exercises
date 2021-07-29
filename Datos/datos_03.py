'''Escribir un programa que pregunte al usuario por el número de horas trabajadas 
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.'''

horas = float(input('¿Cuantas horas has trabajado? : '))
coste = float(input('¿Cuantos euros cobras por hora? :'))

salario = horas * coste

print('Te corresponde una paga de', salario, 'euros' )

