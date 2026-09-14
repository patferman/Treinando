#um aluno é aprovado por média se ele obtiver uma média final maior ou igual a 7, caso o aluno tenha uma 
# média menor que 7 mas maior ou igual a 4 ele está de recuperação, caso ele tenha uma média menor que 4 
# o  aluno está reprovado.



def media(A, B):
    media = (A + B)/2
    return media

A = float(input('digite A: '))
B = float(input('digite B: '))

if media >= 7:
    print('Aprovado')
elif media < 4:
    print('Reprovado')
else:
    print('Recuperacao')




