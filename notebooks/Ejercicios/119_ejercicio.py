
class empleados():
    def __init__(self, nombre, apellido, pago):
        self.nombre = nombre
        self.apellido= apellido
        self.pago = pago
        
    @property
    def email(self):
        return f'{self.nombre}_{self.apellido}.@gmail.com'
    
    @property
    def fullname(self):
        return(f'{self.nombre} {self.apellido}')
    
    def __repr__(self):
        return(f'Empleado('{self.nombre}', '{self.apellido}', '{self.pago}')')