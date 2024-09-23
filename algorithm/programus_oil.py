
def solution(land):
    score = [0, 0]
    dirc = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    index = 1
    r = len(land)
    c = len(land[0])

    for i in range(r):
        for j in range(c):
            if land[i][j] == 1:
                index += 1
                q = [[i, j]]
                land[i][j] = index
                tempScore = 1

                while len(q) > 0:
                    temp = q.pop(0)

                    for d in dirc:
                        dy = temp[0] + d[0]
                        dx = temp[1] + d[1]
                        if dy >= 0 and dy < r and dx >= 0 and dx < c:
                            if land[dy][dx] == 1:
                                land[dy][dx] = index
                                tempScore += 1
                                q.append([dy, dx])

                score.append(tempScore)

    # for i in land:
    #     print(i)
    # print(score)

    answer = 0
    for j in range(c):
        temp = 0
        visited = []
        for i in range(r):
            if land[i][j] != 0 and land[i][j] not in visited:
                visited.append(land[i][j])
                temp += score[land[i][j]]
        if answer < temp:
            answer = temp

    return answer
