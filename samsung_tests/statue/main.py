import sys
from collections import defaultdict
from itertools import combinations


def init() -> None:
    global beamIDLen
    global idIndex
    global twoBeamData

    beamIDLen = [0]*200
    idIndex = 0
    twoBeamData = defaultdict(list)


def addBeam(mLength: int) -> None:
    global beamIDLen
    global idIndex
    global twoBeamData

    beamIDLen[idIndex] = mLength

    for i in range(idIndex):
        twoBeamData[mLength+beamIDLen[i]].append([i, idIndex])

    idIndex += 1


def findAll(height):
    ret = []

    # 두개짜리 가져오기
    if height in twoBeamData:
        for i in twoBeamData[height]:
            ret.append([i[0], i[1]])

    # 하나, 3개 짜리 가져오기
    for i in range(idIndex):
        if beamIDLen[i] == height:
            ret.append([i])
        elif height-beamIDLen[i] in twoBeamData:
            for k in twoBeamData[height-beamIDLen[i]]:
                if i != k[0] and i != k[1]:
                    ret.append([i, k[0], k[1]])
    # print(ret)

    return ret


def requireSingle(mHeight: int) -> int:
    retList = findAll(mHeight)

    ret = 100000001

    for i in retList:
        tempMax = max([beamIDLen[k] for k in i])
        if tempMax < ret:
            ret = tempMax

    if ret == 100000001:
        ret = -1

    # print(ret)
    return ret


def requireTwin(mHeight: int) -> int:
    retList = findAll(mHeight)

    ret = 100000001

    for first, second in list(combinations(retList, 2)):
        temp = []
        checker = False
        for i in first:
            if i in second:
                checker = True
                break

        if checker:
            continue

        # 되는 조합
        tempMax = max([beamIDLen[k] for k in first+second])
        if tempMax < ret:
            ret = tempMax

    if ret == 100000001:
        ret = -1

    # print(ret)
    return ret


##########################################################################################

CMD_INIT = 100
CMD_ADD_BEAM = 200
CMD_REQUIRE_SINGLE = 300
CMD_REQUIRE_TWIN = 400


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            init()
            okay = True
        elif cmd == CMD_ADD_BEAM:
            mLength = int(next(input_iter))
            addBeam(mLength)
        elif cmd == CMD_REQUIRE_SINGLE:
            mHeight = int(next(input_iter))
            ret = requireSingle(mHeight)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_REQUIRE_TWIN:
            mHeight = int(next(input_iter))
            ret = requireTwin(mHeight)
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
