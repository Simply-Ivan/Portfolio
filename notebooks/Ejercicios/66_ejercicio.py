
# Comprobar si una cadena termina con la extersión .py, sino es así, agregar la extensión

def validar_nombre_archivo(n):
    separar = n.split('.')
    if separar[-1] == 'py':
        return n
    else:
        return f'{n}.py'
    
print(validar_nombre_archivo('main.py'))
print(validar_nombre_archivo('modulo'))
