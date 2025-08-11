def soma_primos(n):
    sieve = [True] * n
    sieve[0] = sieve[1] = False

    import math

    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p*p, n, p):
                sieve[i] = False

    
    return sum(i for i, primo in enumerate(sieve) if primo)


print(soma_primos(2_000_000))