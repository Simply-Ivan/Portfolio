class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print('Estudiando ...')

nombre = input('Dame el nombre del estudiante: ')
edad = input('Dame la edad del estudiante: ')
grado = input('Dame el grado del estudiante: ')

estudiante = Estudiante(nombre, edad, grado)

print(f'''
      DATOS DEL ESTUDIANTE:\n
      Nombre: {estudiante.nombre}\n
      Edad: {estudiante.edad}\n
      Grado: {estudiante.grado}\n
      
      ''')

while True:
    estudiar = input()
    if (estudiar.lower() == 'estudiar'):
        estudiante.estudiar()