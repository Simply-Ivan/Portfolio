
# Calcular el volumen de una esfera a partir del radio dado.

import numpy as np

radio = int(input('Dame un radio para hallar el volumen:\t'))

volumen = 4/3 * np.pi * (radio**3)

print(f'El volumen es: {volumen}u^3')