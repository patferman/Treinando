def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

# Entrada do usuário como string
entrada = input("Digite uma lista de números separados por vírgula: ")

# Converter para lista de inteiros
numbers = [int(x) for x in entrada.split(",")]

# Verificar se a lista tem exatamente 5 números
if len(numbers) != 5:
    print("Você deve digitar exatamente 5 números.")
else:
    result = sum_two_smallest_numbers(numbers)
    print(f"A soma dos dois menores números é: {result}")
