#My Solution

#Define a função "multiplo" que verifica se um número n é um múltiplo de m
def multiplo(n,m):

    #Retorna True se o resto da divisão de n por m é zero, o que significa que n é divisível por m
    return n % m == 0

#Define a função "soma_multiplos" que retorna a soma de todos os números menores que um limite que são múltiplos de 3 ou 5
def soma_multiplos(limite):

    #Inicializa a variável "soma" com zero
    soma = 0

    #Itera através de cada número inteiro de 0 até limite - 1
    for n in range(limite):

        #Verifica se n é um múltiplo de 3 ou 5 usando a função multiplo
        if multiplo(n, 3) or multiplo(n, 5):

            #Se n for um múltiplo de 3 ou 5, adiciona-o à variável soma
            soma += n

    #Retorna o valor final da variável soma
    return soma

#Chama a função soma_multiplos com um limite de 1000 e imprime o resultado
print(soma_multiplos(1000))