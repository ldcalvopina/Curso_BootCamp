#Programacion Orientado a Objetos - POO

class Coche:
    
    #Metodo constructor
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def acelerar(self):
        return(f"El coche {self.marca} {self.modelo} de color {self.color} esta acelerando")
        #print(f"El coche {self.marca} {self.modelo} de color {self.color} esta acelerando")

    def frenar(self):
        return (f"El coche {self.marca} {self.modelo} de color {self.color} esta frenando")
    
    def __str__(self):
        return(f"El coche {self.marca} {self.modelo} de color {self.color}")   
    
coche = Coche("Mazda", "CX5", "Rojo")
#print(coche.marca)
coche.acelerar() #esto es cuando en la funcion tiene un print
print(coche.acelerar()) #esto es cuando en la funcion tiene un return
frenar = coche.frenar()
print(frenar)

print(coche.__str__()) 