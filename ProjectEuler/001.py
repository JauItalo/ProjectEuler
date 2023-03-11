#My Solution

def multiplo(n,m):
    return n % m == 0

def soma_multiplos(limite):
    soma = 0
    for n in range(limite):
        if multiplo(n, 3) or multiplo(n, 5):
            soma += n
    return soma

print(soma_multiplos(1000))