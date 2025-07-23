
'''
Crear clase estudiante con los atributos nombre, edad y grado.
'''

class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre = input("Ingresa el nombre dle estudiante: ")
edad = int(input("Ingresa la edad del estudiante: "))
grado = input("Ingresa el grado del estudiante: ")
        
estudiante1 = Estudiante(nombre,edad,grado)

estudiante1.estudiar()
