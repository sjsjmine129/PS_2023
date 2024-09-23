[m, n] = map(int, input().split())

mountain = []
mountain.append([10001]*(n+2))

record = []
record.append([-1]*(n+2))

for i in range(m):
    temp = [int(i) for i in input().split()]
    temp.insert(0, 10001)
    temp.append(10001)

    temp2 = [-2]*n
    temp2.insert(0, -1)
    temp2.append(-1)

    mountain.append(temp)
    record.append(temp2)

mountain.append([10001]*(n+2))
record.append([-1]*(n+2))

dirc = [[0, 1], [1, 0], [0, -1], [-1, 0]]

record[m][n] = 1


def findRoot(y, x):
    nowHeight = mountain[y][x]

    value = 0

    for i in dirc:
        dy = i[0]
        dx = i[1]
        nextHeight = mountain[y+dy][x+dx]
        rec = record[y+dy][x+dx]

        if nextHeight < nowHeight and rec != -1:
            if rec != -2:  # already record
                value += rec
            elif rec == -2:  # have to calculate
                value += findRoot(y+dy, x+dx)

    record[y][x] = value
    return value


print(findRoot(1, 1))
