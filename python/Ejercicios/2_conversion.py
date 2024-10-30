"""
Este script convierte una temperatura ingresada por el usuario de fahrnheit a celsius o de celsius a fahrenget,
dependiendo de la escala proporcionada

"""
print("--BIENVENIDOS AL CONVERTIDOR DE TEMPERATURA")
print("1.- fahrenheit a celsius")
print("2.- celsius a fahrenheit")
opcion = int(input("Ingrese la opcion que quiere utilizar: "))

if opcion==1:
    temperatura = float(input("Ingrese su temperatura: "))
    conver_facel=((temperatura-32)*5/9)
    print("Su temperatura es: ", conver_facel)
elif opcion==2:
    temperatura = float(input("Ingrese su temperatura: "))
    conver_celfa=((temperatura*9/5)+32)
    print("Su temperatura es: ", conver_celfa)
else:
    print("Opcion ingresada incorrectamente")

