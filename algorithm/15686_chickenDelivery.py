from itertools import combinations

N, M = input().split()
n = int(N)
m = int(M)

city = []
for i in range(n):
    temp = [int(i) for i in input().split()]
    city.append(temp)

chicken = []
home = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])


case = list(combinations(chicken, m))


result = []


for ch in case:
    sum = 0
    for ho in home:
        dis = []
        for k in ch:
            dis.append(abs(k[0]-ho[0])+abs(k[1]-ho[1]))
        sum += min(dis)
    result.append(sum)

print(min(result))
