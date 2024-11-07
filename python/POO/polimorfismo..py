class Deporte:
    def jugar(self):
        pass
    
class Futbol(Deporte):
    def jugar(self):
        print(f"Jugando Futbol")

class Baloncesto(Deporte):
    def jugar(self):
        print(f"Jugando Baloncesto")
        
class Tenis(Deporte):
    def jugar(self):
        print(f"Jugando tenis")

deporte1 = Futbol()
deporte1.jugar()

deporte2 = Baloncesto()
deporte2.jugar()

deporte3 = Tenis()
deporte3.jugar()
