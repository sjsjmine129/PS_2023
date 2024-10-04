import sys
from typing import List
from collections import defaultdict


class Result:
    def __init__(self) -> None:
        self.ID: int = 0
        self.height: int = 0
        self.used: int = 0


def init(N: int, mWidth: int, mHeight: int, mIDs: List[int], mLengths: List[List[int]],
         mUpShapes: List[List[int]]) -> None:
    global bukets
    global w
    global h
    global n
    w = mWidth
    h = mHeight
    n = N

    temp = defaultdict(list)

    # 각 어항 초기화
    for i in range(n):
        temp[mIDs[i]] = [[mLengths[i][j], mUpShapes[i][j]] for j in range(w)]

    sortedID = []
    for i in temp:
        sortedID.append(i)
    sortedID.sort()

    bukets = {}
    for i in sortedID:
        bukets[i] = temp[i]

    # print(bukets)
    # for i in bukets:
    #     print(i)


# 결합부 & 붙는지 & 높이
def checkStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:

    ret = 0
    for p in bukets:
        bucketID = bukets[p]

        for nowW in range(w-2):
            # 결합부 확인
            if bucketID[nowW][1] == mDownShapes[0] and bucketID[nowW+1][1] == mDownShapes[1] and bucketID[nowW+2][1] == mDownShapes[2]:
                # 높이 확인
                if bucketID[nowW][0] + mLengths[0] <= h and bucketID[nowW+1][0] + mLengths[1] <= h and bucketID[nowW+2][0] + mLengths[2] <= h:
                    # 붙는지 확인
                    range1 = [bucketID[nowW][0]+1,
                              bucketID[nowW][0]+mLengths[0]]
                    range2 = [bucketID[nowW+1][0]+1,
                              bucketID[nowW+1][0]+mLengths[1]]
                    range3 = [bucketID[nowW+2][0]+1,
                              bucketID[nowW+2][0]+mLengths[2]]

                    if range1[0] <= range2[1] and range1[1] >= range2[0] and range3[0] <= range2[1] and range3[1] >= range2[0]:
                        ret += 1

    # print(ret)
    return ret


def addStructures(mLengths: List[int], mUpShapes: List[int], mDownShapes: List[int]) -> int:
    retID = 0
    retW = -1

    # 설치 위치 찾기
    for p in bukets:
        bucketID = bukets[p]
        checker = False
        for nowW in range(w-2):
            # 결합부 확인
            if bucketID[nowW][1] == mDownShapes[0] and bucketID[nowW+1][1] == mDownShapes[1] and bucketID[nowW+2][1] == mDownShapes[2]:
                # 높이 확인
                if bucketID[nowW][0] + mLengths[0] <= h and bucketID[nowW+1][0] + mLengths[1] <= h and bucketID[nowW+2][0] + mLengths[2] <= h:
                    # 붙는지 확인
                    range1 = [bucketID[nowW][0]+1,
                              bucketID[nowW][0]+mLengths[0]]
                    range2 = [bucketID[nowW+1][0]+1,
                              bucketID[nowW+1][0]+mLengths[1]]
                    range3 = [bucketID[nowW+2][0]+1,
                              bucketID[nowW+2][0]+mLengths[2]]

                    if range1[0] <= range2[1] and range1[1] >= range2[0] and range3[0] <= range2[1] and range3[1] >= range2[0]:
                        retID = p
                        retW = nowW
                        checker = True
                        break
        if checker:
            break

    if retID != 0:
        # 설치해서 데이터 바꾸기
        bukets[retID][retW][0] += mLengths[0]
        bukets[retID][retW+1][0] += mLengths[1]
        bukets[retID][retW+2][0] += mLengths[2]
        bukets[retID][retW][1] = mUpShapes[0]
        bukets[retID][retW+1][1] = mUpShapes[1]
        bukets[retID][retW+2][1] = mUpShapes[2]

    # print(retID*1000 + retW + 1)
    # printAll()
    return retID*1000 + retW + 1


def pourIn(mWater: int) -> Result:
    ret = Result()
    ret.ID = ret.height = ret.used = 0

    for p in bukets:
        bucketData = bukets[p]

        # 층별 물체울 공간
        filledHeightData = [w for _ in range(h)]
        for i in bucketData:
            for j in range(i[0]):
                filledHeightData[j] -= 1

        # 물 채우기
        usedWater = 0
        maxHeight = 0
        for i in range(h):
            need = filledHeightData[i]
            if usedWater + need <= mWater:
                usedWater += need
                maxHeight = i+1
            else:
                break
        if usedWater > 0:
            if maxHeight > ret.height or (maxHeight == ret.height and usedWater > ret.used):
                ret.ID = p
                ret.height = maxHeight
                ret.used = usedWater

    # print(ret.ID,  ret.height, ret.used)
    # print(bukets[ret.ID])
    return ret

#########################################################################################################################################################


def input():
    return sys.stdin.readline().rstrip()


CMD_INIT = 1
CMD_ADD = 2
CMD_CHECK = 3
CMD_POUR = 4

MAX_N = 20
MAX_WIDTH = 500


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mWidth = int(next(input_iter))
            mHeight = int(next(input_iter))
            mIDs = [int(next(input_iter)) for i in range(N)]
            mLengths_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mLengths_tanks.append([int(next(input_iter))
                                      for i in range(mWidth)])
            mUpShapes_tanks = []
            for i in range(N):
                input_iter = iter(input().split())
                mUpShapes_tanks.append([int(next(input_iter))
                                       for i in range(mWidth)])
            init(N, mWidth, mHeight, mIDs, mLengths_tanks, mUpShapes_tanks)
            okay = True
        elif cmd == CMD_CHECK:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = checkStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_ADD:
            mLengths = [int(next(input_iter)) for i in range(3)]
            mUpShapes = [int(next(input_iter)) for i in range(3)]
            mDownShapes = [int(next(input_iter)) for i in range(3)]
            ret = addStructures(mLengths, mUpShapes, mDownShapes)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_POUR:
            mWater = int(next(input_iter))
            ret = pourIn(mWater)
            ans = int(next(input_iter))
            ans_height = 0
            ans_used = 0
            if ans != 0:
                ans_height = int(next(input_iter))
                ans_used = int(next(input_iter))
            if ans != 0 and ((ans != ret.ID) or (ans_height != ret.height) or (ans_used != ret.used)):
                okay = False
            elif ans == 0 and ret.ID != 0:
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
