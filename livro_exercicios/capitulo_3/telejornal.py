programacao = {
    "BomDia": ['Ze Pinheiro', "Ana Carla Araujo"],
    "JornalBrasileiro": ['Bill Bonner', 'Carla Vasconcelos']
}
print(programacao["BomDia"][1])  # Saída: 9.0

"""estruturas aninhadas - dicionario onde o valor são listas"""


busca = input("Digite o nome que quer procurar: ")

for jornal, lista in programacao.items():

    if busca in lista:

        print(f'{busca} apresenta o jornal {jornal}')
        break
else:
    print("Nome não encontrado.")

#for jornal, nome in programacao.items():
#    print(f'nOs nomes são {jornal.title()} são: ')
#    for nome in nome:
#        print(f'\{nome.title()}')

#for jornal, nome in programacao.items():
#    if busca in nome.items():
#       print(f'O jornal em que {nome} trabalha é {jornal.title()}')        
