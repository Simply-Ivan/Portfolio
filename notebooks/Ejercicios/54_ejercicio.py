
# Obtener la extensión de un archivo especificado por el usuario

nombre_archivo = input('Dame el nombre del archivo:\n')
extension_archivo = nombre_archivo.split('.')
print(extension_archivo)
print(extension_archivo[-1])