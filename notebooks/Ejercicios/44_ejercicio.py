
diccionario = {
    'trabajo' : 'minero',
    'animal' : 'león',
    'estudio' : 'medicina',
    'edad' : 18,
    'celular' : 900938586,
    'nombre' : 'Joel',
    'ave' : 'gallito de las rocas'}

claves = diccionario.keys()
valor = diccionario.get('edad')
diccionario.pop('estudio')
diccionario.clear()

print(diccionario)