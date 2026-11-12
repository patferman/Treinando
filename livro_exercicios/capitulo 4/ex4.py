
nome = 'Patricia'
erros = 0

while erros < 4:
    senha = int(input('digite a senha: '))

    if senha == 123456:
        print(f'Olá, {nome}. Benvindo ao nosso banco.')
        break
    else:
        erros +=1
        if erros < 3:
            print('você só tem 3 tentativas. Depois, a senha será bloqueada.')

else:
    print("senha bloqueada")      

