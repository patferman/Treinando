equipe = {
    'jorge': '81.9',
    'maria': '80.4',
    'renata': '85.3',
    'antonio': '79.6',
    'felipe': '79.8',
    'ana': '82.6',
    'Bete': '79.3',

    }
#for chave, valor in equipe.items():
#    print(f'O atleta {chave} teve o tempo de {valor}s.')

#ordenado = dict(sorted(equipe.items(), key= lambda item: item[1], reverse=True))
#print(ordenado)

mais_rapido = min(equipe, key=lambda nome: float(equipe[nome]))

print(f"O atleta mais rápido é {mais_rapido} com o tempo de {equipe[mais_rapido]}s.")


mais_lento = max(equipe, key=lambda nome: float(equipe[nome]))

print(f"O atleta mais lento é {mais_lento} com o tempo de {equipe[mais_lento]}s.")