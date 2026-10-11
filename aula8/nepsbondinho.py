#A primeira linha da entrada contém um inteiro 

#A, representando a quantidade de alunos. A segunda linha da entrada contém um inteiro 

#M, representando o número de monitores.

#Saída
#Seu programa deve imprimir uma linha contendo o caractere #S se é possível levar todos os alunos e monitores em apenas uma viagem, ou o caractere 

#N caso não seja possível.

#Restrições
#1≤A≤50

#1≤M≤50



def bondinho (A, M):

    soma = A + M
    if soma <= 50:
        print('S')
    else:
        print('N')
    
bondinho(8,49)

   
