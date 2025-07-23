
# Resolver la expresión algebraica (x + y) * (x + y)

def resolver(x, y):
    operar = x**2 + 2 * x * y + y**2
    return f'Al operar x y y el resultado es: {operar}'

x_value = float(input('Dame un valor para x: '))
y_value = float(input('Dame un valor para y: '))

print(resolver(x_value, y_value))