# *구현

n, l = map(int, input().split())

board = []

for i in range(n):
    temp = list(map(int, input().split()))
    board.append(temp)

ret = 0

for i in range(n):
    now = board[i][0]
    sameHeight = 1
    checker = True

    for j in range(1, n):
        nextStep = board[i][j]

        if now != nextStep:  # 높이가 다를 때
            if not checker:
                break

            if now + 1 == nextStep:  # 전이 낮을 때
                if sameHeight >= l:  # 이전에 l보다 길게 같은 높이가 지속되었을 때
                    sameHeight = 1
                else:  # 충분한 평지가 없을 때
                    checker = False
                    break
            elif now == nextStep + 1:  # 앞이 낮을 때
                if l == 1:
                    sameHeight = 0
                else:
                    checker = False  # 도달 못하면 실패하도록 + 앞으로 동일한 높이가 나오는지 체크하는 용도
                    sameHeight = 1

            else:  # 아예 다를 때
                checker = False
                break

        else:  # 높이 같을 때
            sameHeight += 1
            if not checker and l == sameHeight:
                sameHeight = 0
                checker = True

        now = nextStep

    if checker:
        ret += 1

ret2 = 0
for i in range(n):
    now = board[0][i]
    sameHeight = 1
    checker = True

    for j in range(1, n):
        nextStep = board[j][i]

        if now != nextStep:  # 높이가 다를 때
            if not checker:
                break

            if now + 1 == nextStep:  # 전이 낮을 때
                if sameHeight >= l:  # 이전에 l보다 길게 같은 높이가 지속되었을 때
                    sameHeight = 1
                else:  # 충분한 평지가 없을 때
                    checker = False
                    break
            elif now == nextStep + 1:  # 앞이 낮을 때
                if l == 1:
                    sameHeight = 0
                else:
                    checker = False  # 도달 못하면 실패하도록 + 앞으로 동일한 높이가 나오는지 체크하는 용도
                    sameHeight = 1

            else:  # 아예 다를 때
                checker = False
                break

        else:  # 높이 같을 때
            sameHeight += 1
            if not checker and l == sameHeight:
                sameHeight = 0
                checker = True

        now = nextStep

    if checker:
        ret2 += 1

print(ret + ret2)
