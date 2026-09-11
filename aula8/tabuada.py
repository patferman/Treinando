def multi_table(numero: int) -> str:
    resultado_str = ""
    for i in range(1, 11):
        resultado_str += f"{numero} x {i} = {numero * i}\n"
    return resultado_str

multi_table(5)

