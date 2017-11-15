a = 1
b = 2
num = 0
while(b < 4000000):
    if(b % 2 == 0):
        num = num + b
    b = b + a
    a = b - a
print(num)
