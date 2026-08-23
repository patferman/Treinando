from math import sqrt
x1 = int(input('Digite x1:  '))
x2 = int(input('Digite x2:  '))
y1 = int(input('Digite y1:  '))
y2 = int(input('Digite y2:  '))
 
calculo =((x2 - x1) * (x2 - x1)) + (( y2-y1) * (y2- y1))
d = sqrt (calculo)
print(f'A distância entre os pontos é: {d}   ')


