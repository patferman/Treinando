n = int(input('Digite: '))

p, c, q = input().split()  # aqui, não pede para digitar os numeros -  colcoquei na linha seguinte para testar
#p = 23
#q = 2
#c = '*'

if c == '+':
    resultado = p + q
else:
    resultado = p * q

if resultado <= n:
    print("OK")
else:
    print("OVERFLOW")


