#Define as duas primeiras posições da sequência de Fibonacci
t1 = 0
t2 = 1

#Inicializa a variável soma com zero
soma = 0

#Executa um loop infinito até que o break seja encontrado
while True:

    #Define o próximo número da sequência de Fibonacci
    t3 = t1 + t2

    #Se o número for maior que 4 milhões, sai do loop
    if t3 > 4000000:
        break

    #Se o número for par, adiciona-o à variável "soma"
    if t3 % 2 == 0:
        soma = soma + t3

    #Atualiza as duas primeiras posições da sequência de Fibonacci
    t1 = t2
    t2 = t3

#Atualiza as duas primeiras posições da sequência de Fibonacci
print(soma)


