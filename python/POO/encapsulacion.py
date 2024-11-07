class CuentaBancaria:
    
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo #ponemos en privado
        
    def depositar(self,cantidad):
         self.__saldo += cantidad
    
    def retirar(self, cantidad):
        self.__saldo -= cantidad
    
    def __str__(self):
        return(f"CuentaBancaria de {self.nombre} con saldo {self.__saldo}")
    
cuenta1 = CuentaBancaria("Luis", 100)
cuenta1.depositar(60)
cuenta1.retirar(40)

print(cuenta1.__str__())