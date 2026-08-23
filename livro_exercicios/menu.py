# Programa com menu de opções
print (f' Menu de opções:')
print (f'1. Média ponderada, com pesos 2 e 3, respectivamente')
print(f'2. Quadrado da soma dos 2 números')
print (f'3. Cubo do menor número')
opcao = int(input('Digite a opção desejada:   '))
if opcao == 1:
    n1 = float(input('Digite o primeiro número:   '))
    n2 = float(input('Digite o segundo número:   '))
    media_pond = (n1*2 + n2*3)/5
    print(f'A média ponderada é {media_pond:.2f}')
elif opcao == 2:
    n1 = float(input('Digite o primeiro número:   '))
    n2 = float(input('Digite o segundo número:   '))
    quadrado = (n1 + n2)**2
    print(f'O quadrado da soma é {quadrado:.2f}')
elif opcao == 3:
    n1 = float(input('Digite o primeiro número:   '))
    n2 = float(input('Digite o segundo número:   '))
    menor = min(n1, n2)
    cubo = menor**3
    print(f'O cubo do menor número ({menor}) é {cubo:.2f}')
else:
    print('Opção inválida!')
