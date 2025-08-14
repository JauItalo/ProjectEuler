def collatz_length(n, cache):

    original_n = n
    length = 0


    while n != 1 and n not in cache:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1


    length += cache.get(n, 1)

    cache[original_n] = length
    return length

cache = {}


m_num = 0
m_tam = 0

for i in range(1, 1_000_000):
    tamanho = collatz_length(i, cache)
    if tamanho > m_tam:
        m_tam = tamanho
        m_num = i

print(f"o numero com a maior sequencia é {m_num} com {m_tam} termos")
