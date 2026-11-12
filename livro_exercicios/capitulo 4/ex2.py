
primeiro = int(input('Digite o primeiro termo da PA:   '))
qtdade = int(input('digite a quantidade de termos na PA:   '))
razao =  int(input('Digite a razão da PA:     '))

lista = []     
for i in range (primeiro, qtdade, razao):
    lista.append(i)
print (lista)


#coloquei a PA dentro de uma lista