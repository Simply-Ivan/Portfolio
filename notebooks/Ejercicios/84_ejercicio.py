
# Crear una clase con herencia básica

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Estudiante(Persona):
    def __init__(self, nombre, apellido, nivel):
        super().__init__(nombre, apellido)
        self.nivel = nivel
        
Ivancito = Estudiante('Ivan', 'Gomez', 'universitario')

print(Ivancito.nivel)
print(isinstance(Ivancito, Estudiante))