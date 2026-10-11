#Par ou Ímpar
#Bino e Cino gostam muito de brincar de par ou ímpar. Bino sempre escolhe par e Cino sempre escolhe ímpar.

#Faça um programa para automatizar o resultado o jogo de par ou ímpar. Seu programa deve ler a quantidade de dedos que cada um utilizou e imprimir o nome do ganhador.

#Entrada
#A entrada consiste de duas linhas. A primeira linha contém a quantidade de dedos que Bino utilizou. A segunda linha contém a quantidade de dedos que Cino utilizou.

#Saída
#A saída consiste de uma linha. Caso Bino vença o jogo, imprima "Bino". Caso Cino vença o jogo, imprima "Cino".

#Restrições
#Como Bino e Cino só tem 10 dedos (contando as duas mãos), os valores fornecidos serão valores entre 0 e 10.

bino = int(input("Digite os dedos de Bino (0 a 10): "))
cino = int(input("Digite os dedos de Cino (0 a 10): "))
            
soma = bino + cino

if soma %2 == 0:
    print('Bino')

else:
    print('Cino')    