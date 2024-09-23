n = int(input())

list = []
for i in range(n):
    row = input()
    temp = []
    for i in range(n):
        temp.append([row[i], 0, 0])

    list.append(temp)


way = [[1, 0], [-1, 0], [0, 1], [0, -1]]

sum = 0
q = []
for i in range(n):
    for j in range(n):
        if list[i][j][1] != 1:
            sum += 1
            now = list[i][j][0]
            q.append([i, j])

            while len(q) != 0:
                temp = q.pop()
                for dir in way:
                    x = temp[0]+dir[0]
                    y = temp[1]+dir[1]
                    if x >= 0 and x < n and y >= 0 and y < n and list[x][y][1] != 1 and list[x][y][0] == now:
                        list[x][y][1] = 1
                        q.append([x, y])


sum_2 = 0
for i in range(n):
    for j in range(n):
        if list[i][j][2] != 1:
            sum_2 += 1
            letter = list[i][j][0]
            if letter == 'B':
                now = ['B']
            else:
                now = ['R', 'G']

            q.append([i, j])

            while len(q) != 0:
                temp = q.pop()
                for dir in way:
                    x = temp[0]+dir[0]
                    y = temp[1]+dir[1]
                    if x >= 0 and x < n and y >= 0 and y < n and list[x][y][2] != 1 and list[x][y][0] in now:
                        list[x][y][2] = 1
                        q.append([x, y])

print(sum, sum_2)
