#Ejercicios
"""
1. Crear un ejercicio que me permita saber si una persona es mayor de edad
"""
edad = input("Ingrese su edad: ")
valor=(int (edad) >= 18)
if(valor==True):
    print("La edad es mayor")
else:
    print("La edad es menor")