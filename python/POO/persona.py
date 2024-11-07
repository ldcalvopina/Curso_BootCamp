#POO Persona

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años")
        
persona1 = Persona("Luis", 25)
persona1.saludar()

persona2 = Persona("Leslie", 52)
print(persona2.nombre)
print(persona2.edad)
persona2.saludar()