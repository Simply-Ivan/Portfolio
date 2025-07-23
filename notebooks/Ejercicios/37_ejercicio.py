
n1 = float(input("Ingresar el primer número\n"))
n2 = float(input("Ingresar el segudo número\n"))
n3 = float(input("Ingresar el tercer número\n"))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n3 and n2 >= n1:
    print(n2)
else:
    print(n3)