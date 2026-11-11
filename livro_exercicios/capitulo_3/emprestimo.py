#informar se o cliente pode pedir o emprestimo. 

nomenegativado = input("Seu nome está negativo? ")
if nomenegativado == 1:
    print("Emprestimo negado")
else:
    carteiraassinada =  input("digite 1 - se sim, ou 2 - se não")
if carteiraassinada == 2:
    print("emprestimo negado")
else:
    casapropria =  input("digite 1 - se sim, ou 2 - se não")
if casapropria == 0:
    print('Empretimo negado')
else:
    print('empresstimo concedido')        
