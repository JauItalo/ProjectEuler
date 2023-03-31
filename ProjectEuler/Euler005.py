#Define uma função para encontrar o Máximo Divisor Comum de dois numeros
def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)

#def mmc(a, b):
     #return (a *b) // mdc(a, b)

#Define uma função para encontrar o Mínimo Múltiplo Comum de uma lista de numeros
def mmc_lista(lista):

    #Inicializa o resultado com o primeiro nunmero da lista
    resultado = lista[0]


    #Percorre a lista e encontra o MMc com cada numero
    for i in range(1, len(lista)):
        resultado = (resultado * lista[i]) //  mdc(resultado, lista[i])

    return resultado

if __name__=="__main__":
    lista = [x for x in range(1, 21)] #Aqui ele cria uma lista do 1 ao 20
    resultado = mmc_lista(lista)
    #a =int(input())
    #b =int(input())
    #resultado = mmc(a, b)
    print(resultado) #Imprime o resultado

