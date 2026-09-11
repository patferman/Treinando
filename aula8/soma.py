#Escreva uma função chamada soma_impares que receba um número inteiro positivo n e retorne a soma de 
# todos os números ímpares de 0 até n.

def soma_impares (n):
    soma = 0
    for i in range(n + 1):
        if i % 2 != 0:
            soma += i
    return soma

print(soma_impares(32))  # Exemplo de uso da função

