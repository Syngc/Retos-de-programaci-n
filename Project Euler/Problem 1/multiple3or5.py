def multiplos(x,y):
    num = y
    ans = [num]
    while(num + y < x):
        num = num + y
        ans.append(num)
    return ans

x = 1000
lista1 = multiplos(x,3)
lista2 = multiplos(x,5)
for i in lista1:
    if i not in lista2:
        lista2.append(i)
num = 0
for i in lista2:
    num = num + i
print(num)
