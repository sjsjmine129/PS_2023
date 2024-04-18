# *브루트포스
# *구현

import math
N, M = map(int, input().split())
n = N
m = M

board = []
for i in range(n):
    listTemp = []
    temp = input()
    for j in temp:
        listTemp.append(j)
    board.append(listTemp)

# print(board)

ret = -1


def checkNew(inputStr):
    global ret
    temp = int(inputStr)
    checker = math.sqrt(temp)
    if checker == int(checker) and ret < temp:
        ret = temp

    temp = int(inputStr[::-1])
    checker = math.sqrt(temp)
    if checker == int(checker) and ret < temp:
        ret = temp


maxLen = max(n, m)


while maxLen > 0:
    dx = -1
    dy = -1

    if maxLen == 1:
        dx = 0
        dy = 0
    else:
        if maxLen <= m and maxLen > 1:
            dx = int((m - maxLen)/(maxLen - 1))

        if maxLen <= n and maxLen > 1:
            dy = int((n - maxLen)/(maxLen - 1))

    # 가로
    if dx != -1:
        for x in range(dx+1):  # 칸 사이 간격
            xlen = maxLen + (maxLen - 1) * x  # 총 길이
            for i in range(n):
                for j in range(m - xlen + 1):
                    tempStr = ''
                    for k in range(maxLen):
                        tempStr = tempStr + board[i][j + k + k*x]
                    checkNew(tempStr)

    # 세로
    if dy != -1:
        for y in range(dy+1):  # 칸 사이 간격
            ylen = maxLen + (maxLen - 1) * y  # 총 길이
            for j in range(m):
                for i in range(n - ylen + 1):
                    tempStr = ''
                    for k in range(maxLen):
                        tempStr = tempStr + board[i + k + k*y][j]
                    checkNew(tempStr)

    # 대각선
    if dy != -1 and dx != -1:
        for x in range(dx + 1):
            xlen = maxLen + (maxLen - 1) * x  # 총 길이
            for y in range(dy + 1):  # 칸 사이 간격
                ylen = maxLen + (maxLen - 1) * y  # 총 길이

                for i in range(n - ylen + 1):
                    for j in range(m - xlen + 1):
                        tempStr = ''
                        for k in range(maxLen):
                            tempStr = tempStr + board[i + k + k*y][j + k + k*x]
                        checkNew(tempStr)

                for i in range(ylen - 1, n):
                    for j in range(m - xlen + 1):
                        tempStr = ''
                        for k in range(maxLen):
                            tempStr = tempStr + board[i - k - k*y][j + k + k*x]
                        checkNew(tempStr)

    maxLen -= 1

print(ret)
