
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    
class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado
        
estudiante1 = Estudiante("Juan",20,"5to")

print(estudiante1.nombre)