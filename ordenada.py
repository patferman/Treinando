
n = int(input('Digite :  '))

lista = []

for i in range(0,n):
    lista.append(int(input('Digite os itens: ')))

print(*lista)