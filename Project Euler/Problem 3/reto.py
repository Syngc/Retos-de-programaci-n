import math

primos = [2,3,5,7,11,13,17,19,23,29]

def addPrimo():
    bol = True
    num = primos[-1] + 2
    while(bol):
        bol2 = True
        for j in primos:
            if(num % j == 0):
                bol2 = False
            if(j == primos[-1] and bol2 == True):
                primos.append(num)
                bol = not bol
                return
        num = num + 2

def factores(x):
    maxPrimo = 2
    i = -1
    while(x != 1):
        i = i + 1
        while(x % primos[i] == 0):
            x = int(x / primos[i])
            maxPrimo = primos[i]
        if(primos[i] == primos[-1]):
            addPrimo()
    return maxPrimo

num = 600851475143
ans = factores(int(num))
print(primos)
