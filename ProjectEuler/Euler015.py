
##from math import comb

#n = 20 
#t_passos = 2 * n 
#resp = comb(t_passos, n)

#print(resp)


#===================================#

t = 20

ways = [1] * (t + 1)
for _ in range(t):
    for j in range(1, t + 1):
        ways[j] += ways[j - 1]

print(ways[t])