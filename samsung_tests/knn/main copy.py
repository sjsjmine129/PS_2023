import sys


def init(K: int, L: int) -> None:
    global k
    global l
    global mIDData  # id 의 위치 저장
    global partNum
    global plane

    mIDData = {}
    k = K
    l = L
    partNum = 4000//l
    plane = [[{} for _ in range(partNum)] for _ in range(partNum)]


# 20000
def addSample(mID: int, mX: int, mY: int, mC: int) -> None:
    plane[(mX-1)//l][(mY-1)//l][(mX, mY)] = mC
    mIDData[mID] = (mX, mY, mC)


# 1000
def deleteSample(mID: int) -> None:
    mX, mY, c = mIDData[mID]
    del plane[(mX-1)//l][(mY-1)//l][(mX, mY)]


# 10000
def predict(mX: int, mY: int) -> int:
    ret = 0

    partY = (mY-1)//l
    partX = (mX-1)//l

    find = [[partX, partY], [partX, partY+1], [partX+1, partY], [partX+1, partY+1], [partX-1,
                                                                                     partY], [partX, partY-1], [partX-1, partY-1], [partX+1, partY-1], [partX-1, partY+1]]
    record = []
    count = 0
    # lastNum = 0
    # lastDist = 0

    for nowPartX, nowPartY in find:
        if nowPartX < 0 or nowPartY < 0 or nowPartX >= partNum or nowPartY >= partNum:
            continue

        nowPart = plane[nowPartX][nowPartY]
        for x, y in nowPart:
            c = nowPart[(x, y)]
            dist = abs(mX-x) + abs(mY-y)
            if dist <= l:  # 되는 위치
                record.append([dist, x, y, c])
                count += 1

    if count >= k:
        record.sort(key=lambda x: (x[0], x[1], x[2]))

        color = [0 for _ in range(11)]
        for i in range(k):
            color[record[i][3]] += 1

        for i in range(1, 11):
            if color[i] > color[ret]:
                ret = i
    else:
        ret = -1

    return ret


#########################################################################################################
CMD_INIT = 100
CMD_ADD_SAMPLE = 200
CMD_DELETE_SAMPLE = 300
CMD_PREDICT = 400


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            K = int(next(input_iter))
            L = int(next(input_iter))
            init(K, L)
            okay = True
        elif cmd == CMD_ADD_SAMPLE:
            mID = int(next(input_iter))
            mX = int(next(input_iter))
            mY = int(next(input_iter))
            mC = int(next(input_iter))
            addSample(mID, mX, mY, mC)
        elif cmd == CMD_DELETE_SAMPLE:
            mID = int(next(input_iter))
            deleteSample(mID)
        elif cmd == CMD_PREDICT:
            mX = int(next(input_iter))
            mY = int(next(input_iter))
            ret = predict(mX, mY)
            ans = int(next(input_iter))
            if ret != ans:
                # print("answer", ans, "predict", ret)
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