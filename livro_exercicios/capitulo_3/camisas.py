camisasVendidas = int(input("Camisas vendidas:   "))
valorCamisa = 12.50
valorFinal = camisasVendidas * valorCamisa

if camisasVendidas > 10:
   print(f'Mais que 10 camisas - O valor final será R$ {valorFinal * 0.9}')
   
elif camisasVendidas <= 5:
    print(f'Menos que 5 camisas - O valor final será R$ {valorFinal * 0.97}')
    
else:
    print(f'O valor final será R$ {valorFinal * 0.95}')

    """Dentro de uma f-string, o que está entre {} é avaliado, então o calculo precisa estar dentro das chaves"""