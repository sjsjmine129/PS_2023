import sys
from collections import defaultdict
import heapq

# 5000 * 5000


def init(N: int) -> None:
    global board
    global n
    global tower
    global partSize
    global colorNum
    global partNum

    n = N
    partSize = 100
    partNum = (n-1) // partSize + 1

    board = [[[defaultdict(list) for _ in range(partNum)]
              for _ in range(partNum)] for _ in range(6)]
    tower = {}
    colorNum = [0, 0, 0, 0, 0, 0]


# 50,000 -> 타워는 각 11000개까지
def buildTower(mRow: int, mCol: int, mColor: int) -> None:
    partR = (mRow-1)//partSize
    partC = (mCol-1)//partSize
    # print(partR, partC, n)
    # print(board[0])
    board[0][partR][partC][mRow].append(mCol)
    board[mColor][partR][partC][mRow].append(mCol)
    tower[(mRow, mCol)] = mColor
    colorNum[mColor] += 1
    colorNum[0] += 1


# 1000개까지
def removeTower(mRow: int, mCol: int) -> None:
    partR = (mRow-1) // partSize
    partC = (mCol-1) // partSize

    if (mRow, mCol) not in tower:
        return
    color = tower[(mRow, mCol)]
    board[0][partR][partC][mRow].remove(mCol)
    board[color][partR][partC][mRow].remove(mCol)
    del tower[(mRow, mCol)]

    colorNum[color] -= 1
    colorNum[0] -= 1


# 10,000
def countTower(mRow: int, mCol: int, mColor: int, mDis: int) -> int:
    if colorNum[mColor] == 0:
        return 0

    # 각 꼭짓 점이 속한 구역 찾기 -> 겹치면 통일
    part = set()
    maxRow = min(mRow+mDis, n)
    minRow = max(1, mRow-mDis)
    maxCol = min(mCol+mDis, n)
    minCol = max(1, mCol-mDis)

    part.add(((maxRow-1) // partSize, (maxCol-1) // partSize))
    part.add(((minRow-1) // partSize, (minCol-1) // partSize))
    part.add(((maxRow-1) // partSize, (minCol-1) // partSize))
    part.add(((minRow-1) // partSize, (maxCol-1) // partSize))

    ret = 0
    nowBoard = board[mColor]
    for i in part:
        for j in nowBoard[i[0]][i[1]]:
            if minRow <= j <= maxRow:
                for k in nowBoard[i[0]][i[1]][j]:
                    if minCol <= k <= maxCol:
                        ret += 1

    # print(ret)
    return ret


dirc = [(-1, 0),  (0, -1), (0, 1), (1, 0)]


# 5,000 개 까지
def getClosest(mRow: int, mCol: int, mColor: int) -> int:
    if colorNum[mColor] == 0:
        # print(-1)
        return -1

    partR = (mRow-1) // partSize
    partC = (mCol-1) // partSize

    ret = 100001

    visited = [[False]*partNum for _ in range(partNum)]
    visited[partR][partC] = True
    q = []
    heapq.heappush(q, (0, partR, partC))
    partDis = partNum + 1

    while q:
        nowPart = heapq.heappop(q)
        for r in board[mColor][nowPart[1]][nowPart[2]]:
            for c in board[mColor][nowPart[1]][nowPart[2]][r]:
                dis = abs(r - mRow) + abs(c - mCol)
                if dis < ret:
                    ret = dis
                    partDis = nowPart[0]
        # 주변 구역 추가
        for d in dirc:
            nextR = nowPart[1] + d[0]
            nextC = nowPart[2] + d[1]
            if 0 <= nextR < partNum and 0 <= nextC < partNum and not visited[nextR][nextC]:
                visited[nextR][nextC] = True
                if partDis + 3 > nowPart[0]:
                    heapq.heappush(q, (nowPart[0]+1, nextR, nextC))
    # print(ret)
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
