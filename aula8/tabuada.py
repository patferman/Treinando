#Your goal is to return multiplication tabledef multiplication_table(number):
def multi_table(number: int) -> str:
    linhas = [f"{i} * {number} = {i * number}" for i in range(1, 11)]
    return "\n".join(linhas)

multi_table(5)
print(multi_table(5))
