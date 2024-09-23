n = int(input())

dp = [[1] for i in range(10)]
dp[0][0] = 0

for i in range(1, n):
    for j in range(10):
        if j == 0:
            dp[j].append(dp[1][i-1])
        elif j == 9:
            dp[j].append(dp[8][i-1])
        else:
            dp[j].append(dp[j-1][i-1]+dp[j+1][i-1])

sum = 0
for i in range(10):
    sum += dp[i][n-1]

print(sum % 1000000000)
