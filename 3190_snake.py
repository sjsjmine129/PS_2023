n = int(input())
k = int(input())

b = []
b.append([-1]*(n+2))
for i in range(n):
    temp = [0]*n
    temp.append(-1)
    temp.insert(0, -1)
    b.append(temp)
b.append([-1]*(n+2))

for i in range(k):
    [y, x] = map(int, input().split())
    b[y][x] = 1

l = int(input())
times = []
lastTime = 0
for i in range(l):
    [second_temp, d] = input().split()
    second = int(second_temp)
    temp = second - lastTime
    lastTime = second
    times.append([temp, d])
times.append([100, "L"])

# y,x  D-> +1, L-> -1
dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dirc_index = 0
head = [1, 1]
s = [[1, 1]]
b[1][1] = 2

gameTime = 0

for time in times:
    second = time[0]
    change_dir = time[1]

    # go forward
    checker = False
    for i in range(second):
        gameTime += 1
        next_y = head[0]+dirc[dirc_index][0]
        next_x = head[1]+dirc[dirc_index][1]
        if b[next_y][next_x] == -1 or b[next_y][next_x] == 2:
            checker = True
            break
        else:
            if b[next_y][next_x] == 0:  # if no apple
                temp = s.pop(0)
                b[temp[0]][temp[1]] = 0

            head = [next_y, next_x]
            b[next_y][next_x] = 2  # move head
            s.append([next_y, next_x])  # add snake

    if checker:
        break

    # change dir
    if change_dir == "D":
        dirc_index += 1
        if dirc_index == 4:
            dirc_index = 0
    else:
        dirc_index -= 1
        if dirc_index == -1:
            dirc_index = 3


print(gameTime)
