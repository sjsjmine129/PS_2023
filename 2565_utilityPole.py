n = int(input())

pole = [0]*501

for i in range(n):
    [a, b] = input().split()
    A = int(a)
    B = int(b)
    pole[A] = B

pole = [x for x in pole if x != 0]

# dp
dp = []

for i in range(len(pole)):
    if i == 0:
        dp.append(1)
    else:
        temp = 1
        for j in range(i):
            if pole[j] < pole[i] and dp[j] >= temp:
                temp = dp[j]+1
        dp.append(temp)

ret = n - max(dp)
print(ret)
