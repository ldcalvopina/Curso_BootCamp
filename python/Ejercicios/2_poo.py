"""
Crear la clase Persona, con los atributos: nombre, edad, profesion
crear 2 metodos: saludar, despedirse
crear 2 instancias de la clase persona y mostrar el nombre y el metodo saludar

"""

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def saludar(self):
        return(f"Hola {self.nombre} se que tiene {self.edad} años y eres {self.profesion}")
    
    def despedirse(self):
        return(f"Adiós {self.nombre}")
    
persona1 = Persona("Luis", 25, "Ingeniero")
print(persona1.nombre)
print(persona1.saludar())