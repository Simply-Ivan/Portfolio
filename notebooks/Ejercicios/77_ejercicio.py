
# Calcular el máximo común divisor de dos números

# MCD: El número máximo que divide 2 números

def mcd(x,y):
    mcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x % k == 0 and y % k == 0:
            mcd = k
            break
        
    return mcd

print(mcd(42, 105))

print(5/2)
print(int(5/2))
        
    