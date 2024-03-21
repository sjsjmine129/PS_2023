# *bfs
# *dp
# *map

[n, m] = map(int, input().split())

record = []

for i in range(n):
    temp = [[-2, -2, int(i)] for i in input()]
    record.append(temp)

dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]


q = [[0, 0, 0]]
time = 1
record[0][0][0] = 1

if n == 1 and m == 1:
    print(1)
    exit()

while len(q):
    nextQ = []
    time += 1

    for i in q:
        y = i[0]
        x = i[1]
        didBreak = i[2]

        for d in dirc:
            nY = y + d[0]
            nX = x + d[1]

            if nY == n-1 and nX == m-1:
                print(time)
                exit()

            if nY < 0 or nY >= n or nX < 0 or nX >= m:
                continue

            if record[nY][nX][2] == 0 and record[nY][nX][didBreak] == -2:  # space
                record[nY][nX][didBreak] = time
                nextQ.append([nY, nX, didBreak])
            elif record[nY][nX][2] == 1 and didBreak == 0 and record[nY][nX][1] == -2:
                nextQ.append([nY, nX, 1])
    q = nextQ

print(-1)
