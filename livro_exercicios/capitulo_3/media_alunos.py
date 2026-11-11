#calcular  amedia das notas e informar se  o aluno foi aprovado ou não.


nota1 = float(input('Informe a nota do bimestre 1:   '))
nota2 = float(input('Informe a nota do bimestre 2:   '))
nota3 = float(input('Informe a nota do bimestre 3:   '))

import statistics

notas = [nota1, nota2, nota3]

media = statistics.mean(notas)

print(media)

"""se a nota for maior que 6, ele está aprovado """

if media>=6:
    print('Aprovado.')    
else:
    print('Reprovado.')    