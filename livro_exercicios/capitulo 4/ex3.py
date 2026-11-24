precos = {'captopril': 4.80, 'losartana': 5.70, 'aspirina': 6.90 , 'levotiroxina' : 6.74}
for chave, valor in precos.items(): 
    print(f'Medicamento {chave} -  R${valor: .2f}')

medicamento = min(precos, key=precos.get)
print(f"Medicamento mais barato: {medicamento}: preço R$ {precos[medicamento]:.2f}")


media = sum(precos.values()) / len(precos)
print(f"Média dos preços: R$ {media:.2f}")


"""Em min(precos, key=precos.get), o argumento key diz o que deve ser usado para comparar os itens.

min(precos) percorre os nomes dos medicamentos, que são as chaves do dicionário.
precos.get busca o preço associado a cada nome.
Assim, min compara os preços e retorna o nome do medicamento mais barato.
Neste caso, o resultado é 'captopril', pois custa 4.80."""