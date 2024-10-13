import sys
from typing import List
from collections import defaultdict


def printPlane():
    for i in range(n):
        for j in range(n):
            print(plane[i][j], end=" ")
        print()


def printPatterns():
    for i in patterns:
        print(i, patterns[i])


def printPatternList():
    print(patternList)


def printAll():
    printPlane()
    print("")
    printPatterns()
    print("")
    printPatternList()
    print("")


def makeStr(starData):
    str = ""
    for i in starData:
        str += f"{i[0]}{i[1]}"
    return str


def trun90(starData: List[List[int]]):
    # 90도 회전
    for i in range(7):
        starData[i] = [starData[i][1], 4-starData[i][0]]

    # 정렬
    ret = sorted(starData, key=lambda pair: (pair[0], pair[1]))
    return ret


def getPatterns(starData: List[List[int]]):
    ret = []
    ret.append(makeStr(starData))

    for i in range(3):
        starData = trun90(starData)
        temp = makeStr(starData)
        if temp not in ret:
            ret.append(temp)

    return ret


def init(N: int, mPlane: List[List[int]]) -> None:
    global n
    global plane
    global patterns  # [pattern] = [[행, 열] ... ]
    global patternList  # index -> pattern

    n = N
    patterns = defaultdict(list)
    patternList = [-1, -1]  # 뒤부터 "pattern"의 키 저장
    plane = [[0]*n for _ in range(n)]
    patternListIndex = 1

    # plane 초기화 -> 하나씩 보면서 타일 찾기
    for i in range(n-4):
        for j in range(n-4):
            if plane[i][j] != 0:  # 이미 타일이 있는 경우
                continue

            temp = []
            for k in range(5):
                for l in range(5):
                    if mPlane[i+k][j+l] == 1:
                        temp.append([k, l])

            if len(temp) != 7:  # 타일아님
                continue

            # 타일인 경우 패턴 찾기
            ablePatterns = getPatterns(temp)

            # 패턴 배열중 이미 있는거 있으면 그거에 넣기 & 없으면 새로운 패턴 추가
            checker = 0
            for p in ablePatterns:
                if p in patterns:
                    patterns[p].append([i, j])
                    checker = patterns[p][0]
                    break

            if checker == 0:  # 배열에 새거 없음
                patternListIndex += 1
                newPattern = ablePatterns[0]
                patternList.append(newPattern)
                patterns[newPattern].append(patternListIndex)
                patterns[newPattern].append([i, j])
                checker = patternListIndex

            # 판에 타일 인덱스 표시
            for k in range(5):
                for l in range(5):
                    plane[i+k][j+l] = checker
    # printAll()


def getCount(mPiece: List[List[int]]) -> int:
    temp = []
    for i in range(5):
        for j in range(5):
            if mPiece[i][j] == 1:
                temp.append([i, j])
    ablePatterns = getPatterns(temp)

    ret = 0
    for p in ablePatterns:
        if p in patterns:
            ret = len(patterns[p]) - 1
            break

    # print(ret)
    return ret


def getPosition(mRow: int, mCol: int) -> int:
    index = plane[mRow][mCol]

    ret = 0
    if index != 0:
        first = patterns[patternList[index]][1]
        ret = (first[0]+2)*10000 + first[1]+2

    # print(ret)
    return ret


################################################################################################################################
CMD_INIT = 0
CMD_CNT = 1
CMD_POSITION = 2

MAX_SIZE = 1000

Map = [[0 for _ in range(MAX_SIZE)] for _ in range(MAX_SIZE)]
Piece = [[0 for _ in range(5)] for _ in range(5)]
Data = [0 for _ in range(40000)]


def init_map(N: int):
    global Map, Data
    idx = 0
    x = 0
    for i in range(int(N / 25)):
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(25):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2
        x = x + 25

    dcnt = N % 25
    if dcnt != 0:
        for y in range(N):
            data = Data[idx]
            idx = idx + 1
            bit = 1
            for m in range(dcnt):
                if data & bit != 0:
                    Map[y][x + m] = 1
                else:
                    Map[y][x + m] = 0
                bit = bit * 2


def make_piece(data: int):
    global Piece
    bit = 1
    for i in range(5):
        for k in range(5):
            if data & bit != 0:
                Piece[i][k] = 1
            else:
                Piece[i][k] = 0
            bit = bit * 2


def run():
    global Map, Data, Piece
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            cnt = int(next(input_iter))
            for i in range(0, cnt):
                input_iter = iter(input().split())
                Data[i] = int(next(input_iter))
            init_map(N)
            init(N, Map)
            okay = True
        elif cmd == CMD_CNT:
            Data[0] = int(next(input_iter))
            make_piece(Data[0])
            ans = int(next(input_iter))
            ret = getCount(Piece)
            if ret != ans:
                okay = False
        elif cmd == CMD_POSITION:
            row = int(next(input_iter))
            col = int(next(input_iter))
            ret = getPosition(row, col)
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
