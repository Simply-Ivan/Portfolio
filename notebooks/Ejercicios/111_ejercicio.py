import statistics
import numpy as np

class Personaje:
    def __init__(self, nombre, poder, velocidad):
        self.nombre = nombre
        self.poder = poder
        self.velocidad = velocidad
    
    def __repr__(self):
        return f'{self.nombre} (Fuerza: {self.poder}, Velocidad: {self.velocidad})'
                
    def __add__(self, otro):
        total_poder = round(((self.poder + otro.poder) / 2)** 1.5, 2)
        nombre_final = self.nombre + '-' + otro.nombre.lower()
        total_velocidad = round(((self.velocidad + otro.velocidad) / 2)** 1.5, 2)
        return (nombre_final, total_poder, total_velocidad)
