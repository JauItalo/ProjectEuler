#Inicializa a variável maior com zero
maior = 0

#Loop externo para os números de 100 a 999
for i in range(100, 1000):

    #Loop interno para os números de i a 999
    for j in range(i, 1000):

        #Calcula o produto dos dois números
        produto = i * j

        #Converte o produto para string e verifica se é igual à sua versão invertida
        if str(produto) == str(produto)[::-1]:

            #Se o produto for um palíndromo e maior que o valor atual de maior, atualiza o valor de maior
            if produto > maior:
                maior = produto

#Imprime o maior número palíndromo encontrado
print(maior)