import sys
from collections import defaultdict


def init(N):
    global emptySize
    global emptyData
    global fileData
    global n

    n = N
    emptySize = n
    emptyData = [[1, n]]
    fileData = defaultdict(list)

    return


def add(mId, mSize):
    global emptySize
    global emptyData
    global fileData
    global n

    if emptySize < mSize:  # 안 들어감
        # print(-1)
        return -1

    emptySize -= mSize  # 들어가니 데이터 저장
    ret = emptyData[0][0]  # 첫 빈칸의 시작점이 시작점

    leftSize = mSize
    deleteNum = 0
    for nowEmpty in emptyData:
        nowEmptySize = nowEmpty[1] - nowEmpty[0] + 1
        if nowEmptySize > leftSize:  # 빈칸의 일부 사용하고 끝
            fileData[mId].append([nowEmpty[0], nowEmpty[0] + leftSize - 1])
            nowEmpty[0] += leftSize
            break
        elif nowEmptySize == leftSize:  # 빈칸 다 사용하고 끝
            fileData[mId].append([nowEmpty[0], nowEmpty[1]])
            deleteNum += 1
            break
        else:  # 빈칸 다 사용하고 더 필요
            fileData[mId].append([nowEmpty[0], nowEmpty[1]])
            leftSize -= nowEmptySize
            deleteNum += 1

    # 빈칸 다 쓴놈은 삭제
    emptyData = emptyData[deleteNum:]

    # print(ret)
    return ret


def remove(mId):
    global emptySize
    global emptyData
    global fileData
    global n

    ret = len(fileData[mId])  # 최적화 가능 -> loop 돌면서 길이 세기

    for data in fileData[mId]:
        emptySize += data[1] - data[0] + 1  # 빈칸 크기 증가

        insertIdx = 0
        # 빈칸 위치 찾아서 삽입
        for i in range(len(emptyData)):  # 빈칸 개수 그때그때 체크해서 최적화 가능
            nowEmpty = emptyData[i]
            if nowEmpty[1] < data[0]:
                insertIdx = i + 1
            else:
                break

        # 새 빈칸 삽입
        emptyData.insert(insertIdx, data)

        # 빈칸 합치기
        if insertIdx > 0:
            if emptyData[insertIdx - 1][1] + 1 == emptyData[insertIdx][0]:
                emptyData[insertIdx - 1][1] = emptyData[insertIdx][1]
                emptyData = emptyData[:insertIdx] + emptyData[insertIdx + 1:]
                insertIdx -= 1
        if insertIdx < len(emptyData) - 1:
            if emptyData[insertIdx][1] + 1 == emptyData[insertIdx + 1][0]:
                emptyData[insertIdx][1] = emptyData[insertIdx + 1][1]
                emptyData = emptyData[:insertIdx + 1] + \
                    emptyData[insertIdx + 2:]

    del fileData[mId]  # 파일 데이터 삭제

    # print(ret)
    return ret


def count(mStart, mEnd):
    global emptySize
    global emptyData
    global fileData
    global n

    ret = 0

    # 모든 데이터로 다 확인
    for key, value in fileData.items():
        for data in value:
            if data[0] > mEnd:
                break
            elif data[1] < mStart:
                continue
            else:
                ret += 1
                break

    # print(ret)
    return ret

#################################


CMD_INIT = 1
CMD_ADD = 2
CMD_REMOVE = 3
CMD_COUNT = 4


def run():
    q = int(input())
    okay = False

    for i in range(q):
        inputarray = input().split()
        cmd = int(inputarray[0])

        if cmd == CMD_INIT:
            n = int(inputarray[1])
            init(n)
            okay = True
        elif cmd == CMD_ADD:
            mid = int(inputarray[1])
            msize = int(inputarray[2])
            ans = int(inputarray[3])
            ret = add(mid, msize)
            if ans != ret:
                okay = False
        elif cmd == CMD_REMOVE:
            mid = int(inputarray[1])
            ans = int(inputarray[2])
            ret = remove(mid)
            if ans != ret:
                okay = False
        elif cmd == CMD_COUNT:
            mstart = int(inputarray[1])
            mend = int(inputarray[2])
            ans = int(inputarray[3])
            ret = count(mstart, mend)
            if ans != ret:
                okay = False
        else:
            okay = False

    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
