import sys

def esPalindromo(palabra):
    for i in range(0,int(len(palabra)/2)):
        if palabra[i] != palabra[-1*(i+1)]:
            return False
    return True

maxPalindromo = 0
for i in range(999,100,-1):
    for j in range(999,100,-1):
        num = str(i * j)
        if esPalindromo(num) and maxPalindromo < i * j:
            maxPalindromo = i * j
print(maxPalindromo)
