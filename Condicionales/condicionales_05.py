'''Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o 
superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales 
y muestre por pantallasi el usuario tiene que tributar o no.'''
 
print('*******Comprobador de tributacion*********')
edad = int(input('Introduce tu edad: '))
ingresos = float(input('Introduce tu ingreso mensual: '))

if edad > 18 and ingresos >= 1000:
    print("Tienes que tributar")
else:
    print("No tienes que tributar")