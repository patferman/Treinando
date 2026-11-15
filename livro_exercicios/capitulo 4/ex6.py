equipe = {
'antonio':1.8,
'jorge':1.6,
'maria': 1.5,
'fabio':1.7,
}


menor = min(equipe, key=lambda nome: float(equipe[nome]))

print(f"O aluno mais baixo é {menor} com a altura de {equipe[menor]}m.")


maior = max(equipe, key=lambda nome: float(equipe[nome]))

print(f"O aluno mais alto é {maior} com a altura de {equipe[maior]}m.")

tempos = [float(tempo) for tempo in equipe.values()]

media = sum(tempos) / len(tempos)

print(f"Média das alturas dos alunos é: {media:.2f} m")
