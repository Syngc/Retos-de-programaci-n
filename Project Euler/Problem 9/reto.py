##
# a = m^2 - n^2
# b = mn
# c = m^2 + n^2
# m^2 - n^2 + mn + m^2 + n^2 = 1000
# m(m + n) = 500

n = 3
m = 4
num = 500
aux = m * (m + n)
while aux != 500:
    n = n + 2
    m = n + 1
    aux =  m * (m + n)
    while aux < 500:
        m = m + 2
        aux = m * (m + n)
a = (m*m - n*n)
b = (2*m*n)
c = (m*m + n*n)
ans = a * b * c
print(ans)
