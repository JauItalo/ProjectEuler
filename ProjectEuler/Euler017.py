


ones = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
tens = [0,0,6,6,5,5,5,7,6,6]

total = 0

for i in range(1, 100):
    if i < 20:
        total += ones[i]
    else:
        total += tens[i//10] + ones[i%10]
    

for i in range(100, 1000):
    centenas = ones[i//100] + 7
    resto = i % 100
    if resto == 0:
        total += centenas
    else:
        total += centenas + 3
        if resto < 20:
            total += ones[resto]
        else:
            total += tens[resto//10] + ones[resto%10]

total += 3 + 8

print(total)
