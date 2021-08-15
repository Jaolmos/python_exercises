'''Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.'''

asignaturas = ['matematicas','fisica','quimica','historia','lengua']
notas = []

for asignatura in asignaturas:
    nota = input('Que nota has sacado en '+ asignatura + '?: ')
    
    notas.append(nota)

for i in range(len(asignaturas)):
    print('en',asignaturas[i],'has sacado', notas[i])
    
    
