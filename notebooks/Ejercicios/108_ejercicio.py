
from random import randint

class Tragamonedas:
    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0
    
    def __str__(self):
        return f'Id: {str(self.id)} - Premio: 100'
        
    def jugar(self):
        self.monedas += 1
        numeros = randint(0,9), randint(0,9), randint(0,9)    
        mensaje = ''
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = f'Felicidafes!!! Ganaste {self.premio}'
        else:
            mensaje = 'Mejor suerte para la próxima'
        
        return numeros, mensaje

traga_a = Tragamonedas(1, 100)
traga_b = Tragamonedas(2, 400)

for i in range(100):
    print(traga_a.jugar())
    print(traga_b.jugar())
    
print(traga_a)
    
