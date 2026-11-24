idades = []

while True:
    idade = int(input('Informe a idade do aluno:  '))
    if idade <=0:
        break

    idades.append(idade)        

print(idades)

maior = max(idades)
menor = min(idades)

média = (maior + menor)/2
print(média)