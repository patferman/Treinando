N = 5

gabarito = ['A', 'E', 'D', 'C', 'B']
candidato = []

for i in range(N):
    candidato.append(input())

acertos = 0

for i in range(N):
    if candidato[i] == gabarito[i]:
        acertos += 1

print(acertos)