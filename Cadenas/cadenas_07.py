'''Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.'''

fecha = input("Introduce tu fecha de nacimiento en este formato dd/mm/aaaa: ")

print('dia', fecha[:2])
print('mes', fecha[3:5])
print('años', fecha[6:])

