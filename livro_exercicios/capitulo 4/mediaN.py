n = int(input("Informe um número inteiro positivo: "))

soma = 0

for i in range(n):
    numero = float(input(f"Digite o {i + 1}º número: "))
    soma += numero

media = soma / n
print(f"A média aritmética é {media: .4f}")

'''o .2f faz com que o resultado teha 2 casas depois da virgula'''