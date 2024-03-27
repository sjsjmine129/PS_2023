# *위상정렬

n, m = map(int, input().split())

dependNum = [0]*(n+1)
dependNum[0] = -1
need = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    dependNum[b] += 1
    need[a].append(b)

ret = []
num = 0

while num < n:
    for i in range(1, n+1):
        if dependNum[i] == 0:
            ret.append(i)
            num += 1
            dependNum[i] = -1
            for j in need[i]:
                dependNum[j] -= 1

for i in ret:
    print(i, end=' ')
