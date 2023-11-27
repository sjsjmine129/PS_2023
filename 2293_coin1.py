n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))

dp = [[0 for j in range(k+1)] for i in range(2)]
dp[0][0] = 1
dp[1][0] = 1

# print(dp)

for i in range(n):
    index_now = i % 2
    index_before = 1-index_now

    for now_value in range(1, k+1):

        temp = now_value-coins[i]
        if temp >= 0:
            dp[index_now][now_value] = dp[index_now][temp] + \
                dp[index_before][now_value]
        else:
            dp[index_now][now_value] = dp[index_before][now_value]

# print(dp)
print(dp[(n-1) % 2][k])
