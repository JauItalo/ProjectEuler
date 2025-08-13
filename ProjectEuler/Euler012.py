from math import isqrt


def fatora(n: int):


    f = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        
        d = 3 if d == 2 else d + 2 
    
    if n > 1:
        f[n] = f.get(n, 0) + 1

    return f

def num_divi(fatores: dict) -> int:
    prod = 1
    for e in fatores.values():
        prod *= (e + 1)
    
    return prod

def divi(n: int) -> int:
    return num_divi(fatora(n))

def prim_divi(min_divs: int) -> tuple[int, int, int]:
    n = 1
    while True:
        a, b = n, n + 1

        if a % 2 == 0:
            a //= 2

        else:
            b //= 2
        
        d = divi(a) * divi(b)
        if d > min_divs:
            Tn = n * (n + 1) // 2
            return n, Tn, d
        
        n += 1

n, triangular, d = prim_divi(500)
print(f"n ={n}")
print(f"T_n = {triangular}")
print(f"número de divisores = {d}")