#Define a função fator_primo que retorna o maior fator primo de um número dado
def fator_primo(n):

    #Inicializa o primeiro fator primo com 2
    i = 2

    #Executa um loop enquanto o quadrado do fator primo atual for menor ou igual ao número dado
    while i * i <= n:

        #Se o número não for divisível pelo fator primo atual, passa para o próximo número
        if n % i:
            i += 1

        #Se o número for divisível pelo fator primo atual, divide o número pelo fator primo e volta a verificar se o número ainda é divisível pelo mesmo fator
        else:
            n //= i

    #Retorna o último fator primo encontrado
    return n

#Executa o código apenas se este arquivo for executado diretamente (não se for importado por outro arquivo)
if __name__=="__main__":

    #Define o número para encontrar o maior fator primo
    number = 600851475143

    #Chama a função fator_primo com o número definido acima e armazena o resultado na variável maior_fator
    maior_fator = fator_primo(number)

    #Imprime a mensagem com o número original e o maior fator primo encontrado
    print("maior fator primo de", number, "é:",maior_fator)



