def diferenca_quadrados(n):


    soma_quadrados =sum(i*i for i in range(1, n+1))

    soma = sum(range(1, n+1))
    quadrado_soma = soma ** 2
    return quadrado_soma - soma_quadrados

if __name__ == "__main__":
    print(diferenca_quadrados(100))