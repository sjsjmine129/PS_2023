N = int(input())

map = []

for i in range(N):
    line = input().split()
    for j in range(N):
        line[j] = int(line[j])
    map.append(line)

# print(map)

min = -1
team = []


def checkCase(index, level):
    global min
    if (level == N/2):
        sumA = 0
        sumB = 0

        team2 = []
        for i in range(N):
            if i not in team:
                team2.append(i)

        for k in team:
            for l in team:
                if k != l:
                    sumA += map[k][l]

        for k in team2:
            for l in team2:
                if k != l:
                    sumB += map[k][l]

        if min == -1:
            min = abs(sumA - sumB)
        elif min > abs(sumA - sumB):
            min = abs(sumA - sumB)

        return

    for i in range(index, N):
        team.append(i)
        checkCase(i+1, level+1)
        team.pop()


checkCase(0, 0)

print(min)
