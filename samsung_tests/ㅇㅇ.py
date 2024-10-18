import sys
from collections import defaultdict

# 5000 * 5000
def init(N: int) -> None:
    global board
    global n
    global tower
    global partSize

    n = N
    partSize = 100
    partNum = n // partSize + 1
    if n % partNum == 0:
        partNum -= 1
    board = [ [[ defaultdict(list) for _ in range(partSize)] for _ in range(partSize)] for _ in range(6)]
    tower = {}



# 50,000 -> 타워는 각 11000개까지
def buildTower(mRow: int, mCol: int, mColor: int) -> None:
    partR = mRow//partSize
    partC = mCol//partSize

    board[0][partR][partC][mRow].append(mCol)
    board[mColor][partR][partC][mRow].append(mCol)
    tower[(mRow, mCol)] = mColor

# 1000개까지
def removeTower(mRow: int, mCol: int) -> None:
    partR = mRow // partSize
    partC = mCol // partSize

    color = tower[(mRow,mCol)]
    board[0][partR][partC][mRow].remove(mCol)
    board[color][partR][partC][mRow].remove(mCol)
    del tower[(mRow,mCol)]

# 10,000
def countTower(mRow: int, mCol: int, mColor: int, mDis: int) -> int:
    #각 꼭짓 점이 속한 구역 찾기 -> 겹치면 통일
    part = set()
    maxRow = min(mRow+mDis, n)
    minRow = max(1, mRow-mDis)
    maxCol = min(mCol+mDis, n)
    minCol = max(1, mCol-mDis)

    part.add((maxRow// partSize, maxCol// partSize))
    part.add((minRow// partSize, minCol// partSize))
    part.add((maxRow// partSize, minCol// partSize))
    part.add((minRow// partSize, minCol// partSize))

    ret = 0
    nowBoard = board[mColor]
    for i in part:
        for j in nowBoard[i[0]][i[1]]:
            if  minRow > j or j > maxRow:
                continue

            for k in nowBoard[i[0]][i[1]][j]:
                if minCol <= k <= maxCol:
                    ret += 1

    return ret

# 5,000 개 까지
def getClosest(mRow: int, mCol: int, mColor: int) -> int:
    ret = 0



    return ret


####################################################################################################

CMD_INIT = 0
CMD_BUILD = 1
CMD_REMOVE = 2
CMD_COUMT = 3
CMD_GET = 4


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            init(N)
            okay = True
        elif cmd == CMD_BUILD:
            row = int(next(input_iter))
            col = int(next(input_iter))
            color = int(next(input_iter))
            buildTower(row, col, color)
        elif cmd == CMD_REMOVE:
            row = int(next(input_iter))
            col = int(next(input_iter))
            removeTower(row, col)
        elif cmd == CMD_COUMT:
            row = int(next(input_iter))
            col = int(next(input_iter))
            color = int(next(input_iter))
            dis = int(next(input_iter))
            ret = countTower(row, col, color, dis)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_GET:
            row = int(next(input_iter))
            col = int(next(input_iter))
            color = int(next(input_iter))
            ret = getClosest(row, col, color)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
