import sys
from typing import List


def printAll():
    print("=============")
    print(board)
    for i in board:
        for j in i:
            if j:
                print("1", end=' ')
            else:
                print("0", end=" ")
        print("")


def decode(y, x, length, mCode):
    if mCode[0] != "(":
        for i in range(length):
            for j in range(length):
                if mCode[0] == '0':
                    board[i+y][j+x] = False
                else:
                    board[i+y][j+x] = True
    else:
        mCode = mCode[1:len(mCode)-1]  # 괄호 제거

        # 4 번 하기
        for i in range(4):
            strRverse = []
            numP = 0
            while True:
                now = mCode.pop()
                strRverse.append(now)
                if now == "(":
                    numP -= 1
                elif now == ")":
                    numP += 1

                if numP == 0:
                    break

            # print(strRverse[::-1])
            nextY = y
            nextX = x
            halflen = length//2

            if i < 2:
                nextY += halflen
            if i % 2 == 0:
                nextX += halflen

            decode(nextY, nextX, halflen, strRverse[::-1])


def init(N: int, L: int, mCode: List[str]) -> None:
    global board
    global n
    global l

    n = N
    l = L
    board = [[False]*N for _ in range(N)]

    mCode_temp = mCode[0:L]

    decode(0, 0, n, mCode_temp)
    printAll()


def encode(mCode: List[str]) -> int:
    return -1


def makeDot(mR: int, mC: int, mSize: int, mColor: int) -> None:
    pass


def paint(mR: int, mC: int, mColor: int) -> None:
    pass


def getColor(mR: int, mC: int) -> int:
    return -1


CMD_INIT = 100
CMD_ENCODE = 200
CMD_MAKE_DOT = 300
CMD_PAINT = 400
CMD_GET_COLOR = 500

mCode = [None for _ in range(200001)]
aCode = [None for _ in range(200001)]


def readCode(L, code):
    i = 0
    while i < L:
        buf = input()
        for j in range(len(buf)):
            code[i] = buf[j]
            i += 1
    code[L] = '\0'


def mstrncmp(a, b, n):
    for i in range(n):
        if a[i] != b[i]:
            return False
    return True


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            L = int(next(input_iter))
            readCode(L, mCode)
            init(N, L, mCode)
            okay = True
        elif cmd == CMD_ENCODE:
            ret = encode(mCode)
            ans = int(next(input_iter))
            readCode(ans, aCode)
            if ret != ans or not mstrncmp(aCode, mCode, ans):
                okay = False
        elif cmd == CMD_MAKE_DOT:
            mR = int(next(input_iter))
            mC = int(next(input_iter))
            mSize = int(next(input_iter))
            mColor = int(next(input_iter))
            makeDot(mR, mC, mSize, mColor)
        elif cmd == CMD_PAINT:
            mR = int(next(input_iter))
            mC = int(next(input_iter))
            mColor = int(next(input_iter))
            paint(mR, mC, mColor)
        elif cmd == CMD_GET_COLOR:
            mR = int(next(input_iter))
            mC = int(next(input_iter))
            ret = getColor(mR, mC)
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
