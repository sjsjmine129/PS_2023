import copy
import itertools


def countSafe(lab_in):
    lab = copy.deepcopy(lab_in)

    for i in range(1, n+1):
        for j in range(1, m+1):
            if lab[i][j] == 2:
                q = []
                q.append([i, j])

                while len(q) > 0:
                    temp = q.pop(0)
                    y = temp[0]
                    x = temp[1]

                    for go in dirc:
                        dy = go[0]
                        dx = go[1]
                        if lab[y+dy][x+dx] == 0:
                            lab[y+dy][x+dx] = 3
                            q.append([y+dy, x+dx])

    count = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            if lab[i][j] == 0:
                count += 1
    return count
######################


n, m = map(int, input().split())
lab = []
lab.append([-1]*(m+2))
for i in range(n):
    temp = list(map(int, input().split()))
    temp.append(-1)
    temp.insert(0, -1)
    lab.append(temp)
lab.append([-1]*(m+2))
dirc = [[-1, 0], [0, -1], [0, 1], [1, 0]]

empty = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if lab[i][j] == 0:
            empty.append([i, j])
wallCase = list(itertools.combinations(empty, 3))

ret = 0
for comb in wallCase:
    temp = copy.deepcopy(lab)
    for i in comb:
        temp[i[0]][i[1]] = 1
    safe = countSafe(temp)

    ret = max(safe, ret)

print(ret)
