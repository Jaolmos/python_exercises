"""Escribe un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido
(desde 1 hasta tu edad actual)."""

edad = int(input("introduce los años que tienes: "))

for i in range(edad):
    print("Has cumplido", i+1, "años")
  