mulheres = 0
maiores = 0

while True:

    idade = int(input('Digite sua idade:  '))
    sexo = input('Digite F ou M:   ')  

    if idade <= 0:
        break

    if sexo == 'F' or sexo =='f':
        mulheres += 1
    elif sexo == 'M' or 'm' and idade >=18:
        maiores +=1

print(f'Temos {mulheres} mulheres na turma')
print(f'Temos {maiores} homens maiores de idade na turma')



