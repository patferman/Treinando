acesso = {
    'procopio': '12345',
    'paiva': '54321'
}

usuario = input('Digite o nome de usuário: ')
senha = input('Digite sua senha: ')

if usuario in acesso and acesso[usuario] == senha:
    print('Acesso permitido')
else:
    print('Usuário ou senha inválidos')
