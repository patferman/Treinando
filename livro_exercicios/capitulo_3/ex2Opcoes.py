numero1 = int(input("digite o numero1:   "))
numero2= int(input("digite o numero2:   "))

"""calcular a media ponderda, com peso 2 e 3"""
peso1 = 2
peso2 = 3

media = (numero1 * peso1)  + (numero2*peso2) / (peso1 + peso2)


"""calcular o quadrado da soma dos numeros"""
quadrado = (numero1 + numero2) * (numero1 + numero2)

"""calcular o cubo do menor numero"""

menor = min(numero1, numero2)
cubo = menor

print(f'A média ponderada é {media}')

print (f' O quadrado é {quadrado}')

