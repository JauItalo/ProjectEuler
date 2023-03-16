t1 = 0
t2 = 1
soma = 0
while True:
    t3 = t1 + t2
    if t3 > 4000000:
        break
    if t3 % 2 == 0:
        soma = soma + t3
    t1 = t2
    t2 = t3
print(soma)


