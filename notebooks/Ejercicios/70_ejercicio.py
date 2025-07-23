
# Comprobar si un carácter dado es una vocal

def es_vocal(letra):
    
    vocales = 'aeiou'
    
    vocales = vocales.lower()

    return letra in vocales
        
print(es_vocal('en'))
print(es_vocal('n'))
print(es_vocal('i'))
print(es_vocal('au'))
print(es_vocal('ou'))
print(es_vocal('nt'))