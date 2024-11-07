
#Clase PADRE
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        pass #nada, yo se que aqui no tengo nada, lo voy a utilizar mas adelante asi que no le compiles todavia pa

#esta clase esta heredando de animal    
class Perro(Animal):
    def hablar(self):
        print(f"{self.nombre} puede ladrar")
    
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} puede mauyar")
        
#crear objetos y pasarle un metodo
animal1 = Perro("firulais")
animal2 =Gato("Pepe")

animal1.hablar()
animal2.hablar()