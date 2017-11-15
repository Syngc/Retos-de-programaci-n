import math

primos = [2,3,5,7]

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

def maxPrimos(x):
    while primos[-1] < x:
        addPrimo()

num = 20
maxPrimos(num)
a = primos.pop()
ans = 1
for i in range(0,len(primos)):
    a = int(math.floor(math.log(num) / math.log(primos[i])))
    ans = ans * int(math.pow(primos[i],a))
print(ans)
