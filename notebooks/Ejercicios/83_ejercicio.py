
# Crear una clase para representar laos datos de una persona.

class Personas:
    def __init__(self, nombre, edad, correo):
        self.nombre = nombre
        self.edad = edad
        self.correo = correo
    
    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nCorreo: {self.correo}'
    
edward = Personas('Edward', '53', 'edwardp@gmail.com') 

print(edward)