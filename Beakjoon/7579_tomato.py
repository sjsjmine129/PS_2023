import sys
from collections import deque


[M, N] = sys.stdin.readline().split()
N = int(N)
M = int(M)

q = deque()
newQ = deque()
map = []
no = 0

for i in range(N):
    line = sys.stdin.readline().split()
    map.append(line)
    for j in range(M):
        temp = int(line[j])
        if temp == 1:
            q.append([i, j])
        if temp == -1:
            no += 1

day = 0

all = N*M - no

if len(q) == all:
    print(0)
    exit()


# print(q)

while True:

    day += 1
    # print("day: ", day)

    while len(q) > 0:
        temp = q.popleft()
        # print(temp)

        if temp[0]-1 >= 0:
            if map[temp[0]-1][temp[1]] == '0':
                map[temp[0]-1][temp[1]] = 1
                newQ.append([temp[0]-1, temp[1]])
        if temp[0]+1 < N:
            if map[temp[0]+1][temp[1]] == '0':
                map[temp[0]+1][temp[1]] = 1
                newQ.append([temp[0]+1, temp[1]])
        if temp[1]-1 >= 0:
            if map[temp[0]][temp[1]-1] == '0':
                map[temp[0]][temp[1]-1] = 1
                newQ.append([temp[0], temp[1]-1])
        if temp[1]+1 < M:
            if map[temp[0]][temp[1]+1] == '0':
                map[temp[0]][temp[1]+1] = 1
                newQ.append([temp[0], temp[1]+1])

    if len(newQ) <= 0:
        break

    for i in range(len(newQ)):
        q.append(newQ.popleft())


# print(map)
sum = 0
for i in range(N):
    for j in range(M):
        if map[i][j] == 1 or map[i][j] == '1':
            sum += 1

if sum == all:
    print(day-1)
    exit()

print(-1)
