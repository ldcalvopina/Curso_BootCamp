#POO animal

class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        
    def comer(self):
        return(f"El animal {self.nombre} tiene aproximadamente {self.edad} y es de la especie {self.especie} y actualmente esta comiendo")
    
gato= Animal("Pepe", 2, "gato")
print(gato.nombre)
print(gato.comer())

perro= Animal("Juanita", 2, "perro")
print(perro.nombre)
print(perro.comer())

#eliminando el objeto
del perro
#print(perro.comer())