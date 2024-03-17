import sys
maxint = sys.maxsize

[n, m, x] = map(int, input().split())

bridge = []
for i in range(n+1):
    bridge.append([-1]*(n+1))

for i in range(m):
    [s, e, t] = map(int, input().split())
    bridge[s][e] = t


def findFastWay(start, end):
    record = [maxint]*(n+1)
    record[start] = 0

    q = [start]

    while len(q) > 0:
        now = q.pop(0)

        for i in range(1, n+1):
            if bridge[now][i] == -1:
                continue

            if record[i] > bridge[now][i] + record[now]:
                record[i] = bridge[now][i] + record[now]
                q.append(i)

    return record[end]


def findAlltWay(start):
    record = [maxint]*(n+1)
    record[0] = -1
    record[start] = 0

    q = [start]

    while len(q) > 0:
        now = q.pop(0)

        for i in range(1, n+1):
            if bridge[now][i] == -1:
                continue

            if record[i] > bridge[now][i] + record[now]:
                record[i] = bridge[now][i] + record[now]
                q.append(i)

    return record


ret = findAlltWay(x)

for i in range(1, n+1):
    if i == x:
        continue

    ret[i] = findFastWay(i, x)+ret[i]

# print(ret)
print(max(ret))
