[n, m] = [int(i) for i in input().split()]

e = [[] for _ in range(n)]


for i in range(m):
    temp = [int(i) for i in input().split()]
    e[temp[0]].append(temp[1])
    e[temp[1]].append(temp[0])


visit = [0] * n


def dfs(i, level):
    if level == 5:
        print(1)
        exit()
    else:
        for j in e[i]:
            if visit[j] == 0:
                visit[j] = 1
                dfs(j, level+1)
                visit[j] = 0


for i in range(n):
    visit[i] = 1
    dfs(i, 1)
    visit[i] = 0


print(0)
