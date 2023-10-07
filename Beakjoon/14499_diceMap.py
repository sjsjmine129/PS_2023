[N, M, x, y, K] = input().split()
N = int(N)
M = int(M)
x = int(x)
y = int(y)
K = int(K)

map = []

for i in range(N):
    line = input().split()
    for j in range(M):
        line[j] = int(line[j])
    map.append(line)

commands = input().split()

bottom = 0
up = 0
north = 0
south = 0
east = 0
west = 0

# print(commands)

for i in commands:
    # print(i)
    if i == '1':
        # 동쪽
        if y+1 >= M:
            continue
        else:
            y += 1
            temp = east

            east = up
            up = west
            west = bottom
            bottom = temp
    elif i == '2':
        # 서쪽
        if y-1 < 0:
            continue
        else:
            y -= 1
            temp = west

            west = up
            up = east
            east = bottom
            bottom = temp
    elif i == '3':
        # 북쪽
        if x-1 < 0:
            continue
        else:
            x -= 1

            temp = north
            north = up
            up = south
            south = bottom
            bottom = temp
    elif i == '4':
        # 남쪽
        if x+1 >= N:
            continue
        else:
            x += 1

            temp = south
            south = up
            up = north
            north = bottom
            bottom = temp

    if map[x][y] == 0:
        map[x][y] = bottom
    else:
        bottom = map[x][y]
        map[x][y] = 0

    print(up)
