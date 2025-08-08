def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True 

contador = 0
numero = 1
while contador < 10001:
    numero += 1
    if is_prime(numero):
        contador += 1

if __name__ == "__main__":
    print("O 10001º número primo é:", numero)
