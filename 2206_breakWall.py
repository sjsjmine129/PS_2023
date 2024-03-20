import sys
sys.setrecursionlimit(10**6)

[n, m] = map(int, input().split())

record = []

for i in range(n):
    temp = [[-2, -2, int(i)] for i in input()]
    record.append(temp)

dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def findRoot(y, x, didPassBreakPoint):
    value = []
    passBreakPoint = didPassBreakPoint

    record[y][x][2] = 1

    for i in dirc:
        dy = i[0]
        dx = i[1]

        if y+dy < 0 or y+dy >= n or x+dx < 0 or x+dx >= m:
            continue

        if y+dy == n-1 and x+dx == m-1:
            value.append(1)

        elif record[y+dy][x+dx][2] == 1 and passBreakPoint == 0:  # 부순 경우
            passBreakPoint = 1
            step = -1
            if record[y+dy][x+dx][passBreakPoint] != -2:
                step = record[y+dy][x+dx][passBreakPoint]
            else:
                step = findRoot(y+dy, x+dx, passBreakPoint)

            if step != -1:
                value.append(step + 1)
            passBreakPoint = 0

        elif record[y+dy][x+dx][2] == 0:  # 안 부순 경우
            step = -1
            if record[y+dy][x+dx][passBreakPoint] != -2:
                step = record[y+dy][x+dx][passBreakPoint]
            else:
                step = findRoot(y+dy, x+dx, passBreakPoint)

            if step != -1:
                value.append(step + 1)

    record[y][x][2] = 0

    if len(value) == 0:
        record[y][x][passBreakPoint] = -1
        return -1
    else:
        ret = min(value)
        record[y][x][passBreakPoint] = ret
        return ret


ret = findRoot(0, 0, 0)

if ret == -1:
    print(ret)
else:
    print(ret+1)
