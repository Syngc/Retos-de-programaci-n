import math

def sumaCuadrados(x):
    suma = 0
    for i in range(1,x + 1):
        suma = suma + math.pow(i,2)
    return suma

def cuadradoSuma(x):
    suma = 0
    for i in range(1,x + 1):
        suma = suma + i
    suma = math.pow(suma,2)
    return suma

num = 100
ans = int(cuadradoSuma(num) - sumaCuadrados(num))
print(ans)
