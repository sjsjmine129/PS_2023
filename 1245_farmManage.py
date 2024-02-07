n, m = map(int, input().split())

farm = []
farm.append([-1]*(m+2))
for i in range(n):
    temp = list(map(int, input().split()))
    temp.append(-1)
    temp.insert(0, -1)
    farm.append(temp)
farm.append([-1]*(m+2))

visit = []
visit.append([-1]*(m+2))
for i in range(n):
    temp = [0]*(m)
    temp.append(-1)
    temp.insert(0, -1)
    visit.append(temp)
visit.append([-1]*(m+2))


dire = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]


# (방문한놈은 제외) 순서대로 돌다가 -> 더 큰놈 있으면 패스, 제일 크면 +1,
# 제일 큰데 동일 존재 -> q에 넣음 -> 하나꺼내서 방문 체크 -> 방문 한놈 -> 그만 확인 & 멈추기
#   -> 방문 안한놈 인경우 주변 확인 -> 제일 크면 ok 동일 있으면 q로
# 정상이면 +1

count = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if visit[i][j] == 0:  # 방문 안한 놈
            checker = True
            now = farm[i][j]
            q = [[i, j]]
            visit[i][j] = 2
            changeTo1 = [[i, j]]

            while len(q) > 0 and checker:
                # print("2")
                temp = q.pop(0)
                y = temp[0]
                x = temp[1]

                for k in dire:
                    if farm[y+k[0]][x+k[1]] > now:
                        checker = False
                        break
                    elif farm[y+k[0]][x+k[1]] == now and visit[y+k[0]][x+k[1]] == 1:
                        checker = False
                        break
                    elif farm[y+k[0]][x+k[1]] == now and visit[y+k[0]][x+k[1]] == 0:
                        q.append([y+k[0], x+k[1]])
                        visit[y+k[0]][x+k[1]] = 2
                        changeTo1.append([y+k[0], x+k[1]])

            for z in changeTo1:
                visit[z[0]][z[1]] = 1

            if checker:  # 옥상
                count += 1

print(count)
