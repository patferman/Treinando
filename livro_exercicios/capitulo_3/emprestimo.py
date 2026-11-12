#informar se o cliente pode pedir o emprestimo. 

print('Digite 1 - se sim, ou 2 - se não:  ')

""" precisa colocar o int aqui - sem o int, o numero digitado é considerado string, e não é comprendido no if - else"""

nomenegativado = int(input("Seu nome está negativo? "))

if nomenegativado == 1:
    print("emprestimo negado")

else:
    carteiraassinada =  int(input("Possui carteira assinada?"))
if carteiraassinada == 2:
    print("emprestimo negado")
else:
    casapropria =  int(input("Tem casa propria?"))

if casapropria == 2:
    print('Emprestimo negado')
else:
    print('emprestimo concedido')


        
