import sys
input = sys.stdin.readline
N = int(input())

map = []
check = [[0]*N for _ in range(N)]

for i in range(N):
    line = sys.stdin.readline().split()
    map.append([int(x) for x in line])

# print(map)
x = N//2
y = N//2

# 좌, 하, 우, 상
direction = [[0, -1], [1, 0], [0, 1], [-1, 0]]
blow = [[[-2, 0, 0.05], [0, 2, 0.02], [0, -2, 0.02], [-1, 1, 0.1],
         [-1, -1, 0.1], [0, -1, 0.07], [0, 1, 0.07], [1, 1, 0.01], [1, -1, 0.01]], [[0, 2, 0.05], [2, 0, 0.02], [-2, 0, 0.02], [1, 1, 0.1],
                                                                                    [-1, 1, 0.1], [1, 0, 0.07], [-1, 0, 0.07], [1, -1, 0.01], [-1, -1, 0.01]], [[2, 0, 0.05], [0, 2, 0.02], [0, -2, 0.02], [-1, 1, 0.01],
                                                                                                                                                                [-1, -1, 0.01], [0, -1, 0.07], [0, 1, 0.07], [1, 1, 0.1], [1, -1, 0.1]], [[0, -2, 0.05], [2, 0, 0.02], [-2, 0, 0.02], [1, 1, 0.01],
                                                                                                                                                                                                                                          [-1, 1, 0.01], [1, 0, 0.07], [-1, 0, 0.07], [1, -1, 0.1], [-1, -1, 0.1]]]
dirStep = 3


check[y][x] = 1

out = 0

while True:
    # print(x, y)

    # 0,0도착시 멈춤
    if x == 0 and y == 0:
        break

    # 만약 꺾인다면 가는 곳
    if dirStep == 3:
        dirTemp = 0
    else:
        dirTemp = dirStep+1

    # 만약 꺽인다면 가는 곳이 0이라면 꺾음
    if check[y+direction[dirTemp][0]][x+direction[dirTemp][1]] == 0:
        dirStep = dirTemp

    # 이동
    y = y+direction[dirStep][0]
    x = x+direction[dirStep][1]

    # print("y, x: ", y, x)
    # print("dirStep: ", dirStep)

    # 하는거
    check[y][x] = 1
    # print(map[y][x])
    sand_origin = map[y][x]
    sand_left = sand_origin

    map[y][x] = 0

    # 모래 옮기기
    for move in blow[dirStep]:
        temp_y = y+move[1]
        temp_x = x+move[0]

        if (temp_y < 0 or temp_y >= N or temp_x < 0 or temp_x >= N):
            out += int(sand_origin*move[2])
            sand_left -= int(sand_origin*move[2])
            continue
        else:
            map[temp_y][temp_x] += int(sand_origin*move[2])
            sand_left -= int(sand_origin*move[2])

    # a 부분 옮기기
    temp_y = y+direction[dirStep][0]
    temp_x = x+direction[dirStep][1]
    if (temp_y < 0 or temp_y >= N or temp_x < 0 or temp_x >= N):
        out += sand_left
    else:
        map[temp_y][temp_x] += sand_left

    # print("====================================")
    # for i in range(N):
    #     print(map[i])

    # print("====================================")


print(out)
