import sys


def init(N: int, M: int, mType: list, mTime: list) -> None:
    global n
    global m
    global roadData
    global partSize
    global partNum
    global partSum

    n = N
    m = M

    partSize = min(100, n)
    partNum = (n - 1) // partSize + 1

    roadData = [{} for _ in range(partNum)]
    partSum = [0 for _ in range(partNum)]

    for i in range(n):
        nowPart = i // partSize
        roadData[nowPart][i] = [mTime[i], mType[i]]
        partSum[nowPart] += mTime[i]

    return


def update(mID: int, mNewTime: int) -> None:
    nowPart = mID // partSize
    beforeTime = roadData[nowPart][mID][0]

    # 도로 정보 수정
    roadData[nowPart][mID][0] = mNewTime

    # 부분의 합 수정
    partSum[nowPart] += mNewTime - beforeTime

    return


def updateByType(mTypeID: int, mRatio256: int) -> int:
    ret = 0

    for part in range(partNum):
        newPartSum = 0
        beforePartSum = 0
        for i in roadData[part]:
            if roadData[part][i][1] == mTypeID:
                time = roadData[part][i][0]

                beforePartSum += time
                newTime = (time * mRatio256) // 256
                newPartSum += newTime
                ret += newTime
                roadData[part][i][0] = newTime

        # 부분의 합 수정
        partSum[part] += newPartSum - beforePartSum

    # print(ret)
    return ret


def getPartSum(start: int, end: int) -> int:
    ret = 0
    nowPart = start // partSize

    for i in range(start, end):
        ret += roadData[nowPart][i][0]

    return ret


def calculate(mA: int, mB: int) -> int:
    ret = 0
    if mA > mB:
        start, end = mB, mA
        startPart = mB//partSize
        endPart = mA//partSize
    else:
        start, end = mA, mB
        startPart = mA//partSize
        endPart = mB//partSize

    if startPart == endPart:  # 시작과 끝이 같은 파트
        ret = getPartSum(start, end)
    else:
        ret += getPartSum(start, (startPart + 1) * partSize)
        ret += getPartSum(endPart*partSize, end)
        # 중간 파트의 합들 다 더하기
        for part in range(startPart + 1, endPart):
            ret += partSum[part]

    # print(ret)
    return ret


def destroy() -> None:
    return

########################################################################


MAX_N = 100000

CMD_INIT = 100
CMD_DESTROY = 200
CMD_UPDATE = 300
CMD_UPDATE_TYPE = 400
CMD_CALC = 500

mType = [0 for _ in range(MAX_N)]
mTime = [0 for _ in range(MAX_N)]


def run():
    isOK = 0
    C = int(sys.stdin.readline())
    for c in range(C):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))
        if cmd == CMD_INIT:
            N = int(next(inputs))
            M = int(next(inputs))
            for i in range(N - 1):
                mType[i] = int(next(inputs))
            for i in range(N - 1):
                mTime[i] = int(next(inputs))
            init(N, M, mType, mTime)
            isOK = 1
        elif cmd == CMD_UPDATE:
            mID = int(next(inputs))
            mNewTime = int(next(inputs))
            update(mID, mNewTime)
        elif cmd == CMD_UPDATE_TYPE:
            mTypeID = int(next(inputs))
            mRatio256 = int(next(inputs))
            ret = updateByType(mTypeID, mRatio256)
            check = int(next(inputs))
            if ret != check:
                isOK = 0
        elif cmd == CMD_CALC:
            mA = int(next(inputs))
            mB = int(next(inputs))
            ret = calculate(mA, mB)
            check = int(next(inputs))
            if ret != check:
                isOK = 0
        else:
            isOK = 0
    destroy()
    return isOK


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
