alt1 = float(input("digite a altura de 1: ").replace(",", "."))
alt2 = float(input("digite a altura de 2: ").replace(",", "."))
alt3 = float(input("digite a altura de 3: ").replace(",", "."))

if alt1==alt2 or alt1==alt3 or alt2==alt3:
    print('Há, pelo menos, duas pessoas com a mesma altura.  ')
else:
    maior = max(alt3, alt2, alt1)
    print(f" A maior altura da turma é {maior: .2f}m")        


"""utilizando o replace, para que sejam aceitos tanto a virgula quanto o ponto no input"""