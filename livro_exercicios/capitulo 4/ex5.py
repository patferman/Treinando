equipe = {
    'jorge': '12.9',
    'maria': '13.4',
    'renata': '11.3',
    'antonio': '15.6',
    'felipe': '16.8',
    'ana': '15.6',
    'Bete': '14.3',

    }
#for chave, valor in equipe.items():
#    print(f'O atleta {chave} teve o tempo de {valor}s.')

#ordenado = dict(sorted(equipe.items(), key= lambda item: item[1], reverse=True))
#print(ordenado)

mais_rapido = min(equipe, key=lambda nome: float(equipe[nome]))

print(f"O atleta mais rápido é {mais_rapido} com o tempo de {equipe[mais_rapido]}s.")


mais_lento = max(equipe, key=lambda nome: float(equipe[nome]))

print(f"O atleta mais lento é {mais_lento} com o tempo de {equipe[mais_lento]}s.")

quantidade = 0

for tempo in equipe.values():
    if 12 <= float(tempo) <= 15:
        quantidade += 1

print(f"Quantidade de atletas entre 12 e 15: {quantidade}")