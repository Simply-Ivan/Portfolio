
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f'El nombre de la personas es {self.nombre} y su edad es {self.edad}')
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f'El grado del estudiante es: {self.grado}')
        
estudiante_1 = Estudiante('Carlos', 24, 'primero')

print(estudiante_1.nombre)
print(estudiante_1.edad)
print(estudiante_1.grado)

estudiante_1.mostrar_grado()
estudiante_1.datos()