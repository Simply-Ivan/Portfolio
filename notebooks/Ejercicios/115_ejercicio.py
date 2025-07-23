# Definir un diccionario con los sueldos para cada cargo
sueldos = {
    "Ejecutivo": 90,
    "Jefe": 100,
    "Externo": 50
}

# Ingresar el cargo del trabajador
cargo = "Externo"  # Puedes cambiar esto a cualquier cargo deseado

# Asignar el sueldo correspondiente al cargo
if cargo in sueldos:
    dinero = sueldos[cargo]
else:
    dinero = 0  # Sueldo por defecto si el cargo no existe en la lista

# Imprimir el sueldo asignado
print(f"El sueldo para el cargo de {cargo} es: {dinero} dólares")
