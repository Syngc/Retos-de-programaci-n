import math
num = 100
sumaCuadrados = (num*(num + 1)*(2*num + 1 )) / 6
cuadradoSuma = math.pow(num*(num + 1) /2,2)
ans = cuadradoSuma - sumaCuadrados
print(ans)
