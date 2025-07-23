
# Calcular la distancia entre dos puntos cartesianos.

import numpy as np

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
def calcular_distancia(p1, p2):
    
    return np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

punto1 = Punto(3, 2)
punto2 = Punto(-3, -5)

print(calcular_distancia(punto1, punto2))