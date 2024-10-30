"""
Crear una funcion que pida al usuario 2 notas y devuelva  laa mayor  de ellas

"""
# def notamayor(nota1, nota2):
#     if(nota1>nota2):
#         print(nota1, "es mayor a ", nota2)
#         print(nota2, "es mayor a ", nota1)
#     else:
#         print("Ambos son iguales")

# notamayor(nota1, nota2)

def mayor_nota(nota1, nota2):
  
  
  if(nota1>nota2):
    return nota1
  elif(nota2>nota1):
    return nota2
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
notamayor = mayor_nota(nota1, nota2)
print("La nota mayor es: ", notamayor)