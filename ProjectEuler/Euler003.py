#def number(n):
#    if n % 2 == 0:
#        return 2
#    if n % 2 == 0:
#        return 3
#    if n % 2 == 0:
#        return 4
#    if n % 2 == 0:
#        return 5/
def fator_primo(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

number = 600851475143
maior_fator = fator_primo(number)
print("maior fator primo de", number, "é:",maior_fator)



