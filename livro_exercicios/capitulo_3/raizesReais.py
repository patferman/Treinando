'''Uma equaçáo de segundo grau não tem raizes reais quando o delta é menor que zero, ou seja, negativo. '''

a = int(input("digite o valor de a:  "))
b = int(input("digite o valor de b:  "))
c = int(input("digite o valor de c:  "))

#a*(x**2) + b*x + c = 0

x = (-c-b)/a

if x <=0:
    print('Não existem raízes reais')

else:    
    print (x)
