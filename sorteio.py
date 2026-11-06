#Senha 2018
#Bino desafiou Cino a descobrir o número que ele estava pensando. Bino está pensando no número 2018. Cino vai informar números até que acerte o número que Bino está pensando.
# Faça um programa para receber os números que Cino chutou. Seu programa só deve parar de solicitar um valor quando Cino acertar o 2018.

#Entrada
#A entrada consiste de múltiplas linhas. Cada linha contém um inteiro representando um chute de Cino. É garantido que Cino irá fornecer o valor 2018.

#Saída
#A saída consiste de uma única linha informando quantas vezes Cino errou o número que Bino estava pesando.



import random

aleatorio = (random.randint(0,10))

print(aleatorio)

while True:
    palpite = int(input('digite seu palpite:   '))

    if palpite == aleatorio:
        print("Acertou!")
        break

    elif palpite > aleatorio:
        print("Passou, tente um numero menor!!")


    else:
        print('Tente um numero maior...') 