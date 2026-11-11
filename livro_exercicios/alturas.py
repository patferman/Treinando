alt1 = float(input("digite a altura de 1: ").replace(",", "."))
alt2 = float(input("digite a altura de 2: ").replace(",", "."))
alt3 = float(input("digite a altura de 3: ").replace(",", "."))

print(*sorted([alt1, alt2, alt3]))


"""utilizando o replace, para que sejam aceitos tanto a virgula quanto o ponto no input"""