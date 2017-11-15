primos = [2,3]

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

num = 10001
while(len(primos) < num):
    addPrimo()
    print(str(primos[-1])+' en la posicion '+str(len(primos)))
print(primos[-1])
