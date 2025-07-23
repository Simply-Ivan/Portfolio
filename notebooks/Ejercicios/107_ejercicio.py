

apellido = 'Gomez'

print( apellido[len(apellido)-1] )      # Tomando el ult caracter

apellido = 'Llaccta'

print( apellido[len(apellido)-1] )      # Tomando el ult caracter

nombre = 'Ivan'
apellido = 'Gomez'

nombre_completo = nombre + ' ' + apellido

print(nombre_completo[0:4])
print(nombre_completo[:4])
print(nombre_completo[5:len(nombre_completo)])
print(nombre_completo[5:])

mayuscula = nombre_completo.upper()
minuscula = nombre_completo.lower()

print(mayuscula)
print(minuscula)

# El método strip limpia los espacios

name = '    Ivan Gomez   '
print(name.strip())                     

# El método capitalize coloca la primera letra en mayúscula

print(nombre_completo.capitalize())

# El método replace reemplaza letras

nombre_mal = '1van'
print(nombre_mal.replace('1', 'I'))

# Índice de las palabras

print( nombre_completo.index('o'))

# El método split divide las palabras por lo que designamos
nombre ='Ivan Gomez Pariona'
print(nombre.split()) 
name = 'Ivan_Gomez_Pariona'
print(name.split('_')) 
name1 = 'Ivan.Gomez.Pariona'
print(name1.split('.')) 

