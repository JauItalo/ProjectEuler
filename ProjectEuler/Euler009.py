


for a in range(1, 1000):
    for b in range (a + 1, 1000):
        c = 1000 - a - b
        if c > b and a * a + b * b == c * c:
            print(f"a={a}, b={b}, c={c}")
            print(f"Produto abc = {a * b * c}")