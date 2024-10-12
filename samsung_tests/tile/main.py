import sys
from typing import List
from collections import defaultdict


def printWall():
    for i in wall:
        for j in i:
            if j == 0:
                print(' ', end=' ')
            elif j == 1:
                print('◼︎', end=' ')
            elif j == 2:
                print('▲', end=' ')
            elif j == 3:
                print('●', end=' ')
            elif j == 4:
                print('♦︎', end=' ')
            elif j == 5:
                print('★', end=' ')
            elif j == 11:
                print('◻︎', end=' ')
            elif j == 12:
                print('△', end=' ')
            elif j == 13:
                print('○', end=' ')
            elif j == 14:
                print('♢', end=' ')
            elif j == 15:
                print('☆', end=' ')
            else:
                print('X', end=' ')
        print()


def printPattern():
    for i in boltPattern:
        count = 0
        for j in i:
            count += 1
            if count == 3:
                print("")
                print(" ", end='')
            elif count == 4:
                print("")

            if j == "6":
                print('◼︎',  end=' ')
            elif j == "7":
                print('▲',  end=' ')
            elif j == "8":
                print('●',  end=' ')
            elif j == "9":
                print('♦︎',  end=' ')
            elif j == "0":
                print('★',  end=' ')
            elif j == "1":
                print('◻︎',  end=' ')
            elif j == "2":
                print('△',  end=' ')
            elif j == "3":
                print('○',  end=' ')
            elif j == "4":
                print('♢',  end=' ')
            elif j == "5":
                print('☆',  end=' ')
            else:
                print('*',  end=' ')

        print(":", boltPattern[i])
        print("")


def printRowPattern():
    for i in boltPattern:
        print(i, ":", boltPattern[i])


def init(N: int, mInfo: List[List[int]]) -> None:
    global n
    global wall
    global boltPattern
    global tileData

    n = N
    wall = [[True]*n for _ in range(n)]
    boltPattern = defaultdict(list)
    tileData = {}

    for i in range(n-2):
        for j in range(n-2):
            if mInfo[i][j] != 0:
                temp = [mInfo[i][j], mInfo[i][j+2],
                        mInfo[i+1][j+1], mInfo[i+2][j], mInfo[i+2][j+2]]
                nutNum = 0
                for k in temp:
                    if k > 10:
                        nutNum += 1
                if nutNum < 4:
                    continue

                if nutNum == 4:  # 4개 너트 1개 볼트
                    pattern = ""
                    for k in temp:
                        if k > 10:
                            pattern += str(k-10)
                        else:
                            pattern += str((k+5) % 10)
                    boltPattern[pattern].append((i, j))
                elif nutNum == 5:  # 5개 너트
                    pattern = ""
                    for k in temp:
                        pattern += str(k-10)
                    boltPattern[pattern].append((i, j))
                    for k in range(len(pattern)):
                        temp = pattern[:k] + "*" + pattern[k+1:]
                        boltPattern[temp].append((i, j))

    # printPattern()
    # printRowPattern()
    # exit()


def addRectTile(mID: int,  mTile: List[List[int]]) -> int:
    ret = -1

    # 위치 찾기
    tile = [mTile[0][0], mTile[0][2], mTile[1][1], mTile[2][0], mTile[2][2]]
    # 5개 볼트
    if max(tile) <= 5:
        pattern = ""
        for i in tile:
            pattern += str(i)

        if pattern in boltPattern:
            for ablePosition in boltPattern[pattern]:  # 들어가는 위치 존재
                y = ablePosition[0]
                x = ablePosition[1]
                # 그 위치에 타일이 들어갈 수 있는지 확인
                if wall[y][x] and wall[y][x+2] and wall[y+1][x+1] and wall[y+2][x] and wall[y+2][x+2]:
                    # 타일을 붙인 경우 데이터 조정
                    tileData[mID] = [y, x]

                    # 타일 붙어 있는 곳이라고 표시
                    wall[y][x] = False
                    wall[y][x+2] = False
                    wall[y+1][x+1] = False
                    wall[y+2][x] = False
                    wall[y+2][x+2] = False

                    ret = y*10000 + x
                    break

    else:  # 4개 볼트 1개 너트
        pattern1 = ""
        pattern2 = ""
        for i in tile:
            if i > 10:
                pattern2 += str('*')
                pattern1 += str((i-5) % 10)
            else:
                pattern2 += str(i)
                pattern1 += str(i)
        # print(pattern1, pattern2)

        miny = 999
        minx = 999
        if pattern1 in boltPattern:
            for ablePosition in boltPattern[pattern1]:
                y = ablePosition[0]
                x = ablePosition[1]
                # 그 위치에 타일이 들어갈 수 있는지 확인
                if wall[y][x] and wall[y][x+2] and wall[y+1][x+1] and wall[y+2][x] and wall[y+2][x+2]:
                    miny = y
                    minx = x
                    break
        if pattern2 in boltPattern:
            for ablePosition in boltPattern[pattern2]:
                y = ablePosition[0]
                x = ablePosition[1]
                # 그 위치에 타일이 들어갈 수 있는지 확인
                if wall[y][x] and wall[y][x+2] and wall[y+1][x+1] and wall[y+2][x] and wall[y+2][x+2]:
                    if miny > y:
                        miny = y
                        minx = x
                    elif miny == y and minx > x:
                        miny = y
                        minx = x
                    break

        if miny == 999:
            ret = -1
        else:
            ret = miny*10000 + minx
            wall[miny][minx] = False
            wall[miny][minx+2] = False
            wall[miny+1][minx+1] = False
            wall[miny+2][minx] = False
            wall[miny+2][minx+2] = False
            tileData[mID] = [miny, minx]

    # print(ret)
    return ret


def removeRectTile(mID: int) -> None:
    if mID in tileData:
        y = tileData[mID][0]
        x = tileData[mID][1]
        wall[y][x] = True
        wall[y][x+2] = True
        wall[y+1][x+1] = True
        wall[y+2][x] = True
        wall[y+2][x+2] = True
        del tileData[mID]


#########################################################################################################################################################################################################################
CMD_INIT = 0
CMD_ADD = 1
CMD_REMOVE = 2

MAX_N = 999

dy = (0, 0, 1, 2, 2)
dx = (0, 2, 1, 0, 2)
Shape = (1, 2, 3, 4, 5, 11, 12, 13, 14, 15)

mInfo = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
mData = [[0 for _ in range(3)] for _ in range(3)]

mSeed = 0

N = 0


def pseudo_rand():
    global mSeed
    mSeed = mSeed * 214013 + 2531011
    mSeed = mSeed & 0xffffffff
    return (mSeed >> 16) & 0x7fff


def make_info():
    global N, mInfo, Shape
    for y in range(0, N, 2):
        for x in range(0, N, 2):
            mInfo[y][x] = Shape[pseudo_rand() % 10]
            if y + 1 < N and x + 1 < N:
                mInfo[y + 1][x + 1] = Shape[pseudo_rand() % 10]


def make_info_1():
    global N, mInfo
    for y in range(0, N):
        input_iter = iter(input().split())
        for x in range(0, N):
            mInfo[y][x] = int(next(input_iter))


def run():
    global mSeed, mInfo, mData, N
    mid = 0
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    sample_1 = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mSeed = int(next(input_iter))
            if sample_1 == 1:
                make_info_1()
            else:
                make_info()
            mid = 0
            init(N, mInfo)
            okay = True
        elif cmd == CMD_ADD:
            mid = mid + 1
            for i in range(0, 5):
                mData[dy[i]][dx[i]] = int(next(input_iter))
            ret = addRectTile(mid, mData)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_REMOVE:
            id = int(next(input_iter))
            removeRectTile(id)
        else:
            okay = False
    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    T, MARK = map(int, input().split())

    for tc in range(1, T + 1):
        score = MARK if run() else 0
        print("#%d %d" % (tc, score), flush=True)
