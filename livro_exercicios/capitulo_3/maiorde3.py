#ler 3 numeros e dizer qual o maior.

numero1 = int(input("digite o numero1:   "))
numero2 = int(input("digite o numero2:   "))
numero3 = int(input("digite o numero3:   "))

if numero1 == numero2 == numero3:
    print('Todos são iguais')

if numero1>numero2 and numero1>numero2:
    print('numero 1 é o maior.')  
elif numero2>numero1 and numero2>numero3:
    print('numero 2 é o maior.')
else:
    print('numero 3 é o maior.')    
