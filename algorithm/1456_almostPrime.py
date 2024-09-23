[N, M] = input().split()
n = int(N)
m = int(M)

primeList = [True] * (int(m ** 0.5) + 1)
primeList[1] = False

#
for i in range(2, (int(m ** 0.5) + 1)):
    if primeList[i]:
        if i*i > int(m ** 0.5):
            break
        else:
            for j in range(i**2, int(m ** 0.5) + 1, i):
                primeList[j] = False

ret = 0
for i in range(2, (int(m ** 0.5) + 1)):
    if primeList[i]:
        num = i * i
        while num <= m:
            if num >= n and num <= m:
                ret += 1
            num = num * i

print(ret)
