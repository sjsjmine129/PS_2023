import sys


# 5000 * 5000
def init(N: int) -> None:
    global board

    board = [[[-1]*5000 for _ in range(5000)] for _ in range(6)]


# 50,000 -> 타워는 각 11000개까지
def buildTower(mRow: int, mCol: int, mColor: int) -> None:
    pass

# 1000개까지


def removeTower(mRow: int, mCol: int) -> None:
    pass

# 10,000


def countTower(mRow: int, mCol: int, mColor: int, mDis: int) -> int:
    return 0

# 5,000 개 까지


def getClosest(mRow: int, mCol: int, mColor: int) -> int:
    return 0


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
