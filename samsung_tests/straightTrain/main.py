import sys

from collections import defaultdict
import heapq


def init(N, K, mId, sId, eId, mInterval):
    global n
    global k
    global graph
    global ids
    n = N
    k = K
    ids = {}
    graph = defaultdict(list)

    for i in range(k):
        add(mId[i], sId[i], eId[i], mInterval[i])

    return


def add(mId, sId, eId, mInterval):
    # 열차 데이터 저장
    ids[mId] = [sId, eId, mInterval]

    # 연결된 열차들 저장
    for j in ids:
        train = ids[j]
        if j == mId:  # 본인이면 스킵
            continue

        # 다른 열차로 갈아탈 수 있는지
        now = sId
        compare = train[0]
        while now <= eId and compare <= train[1]:
            if now == compare:  # 역이 겹침
                # 에지 추가
                graph[j].append(mId)
                graph[mId].append(j)
                break
            elif now > compare:  # com 가 작음
                compare += train[2]
            elif now < compare:  # now 가 작음
                now += mInterval

    return


def remove(mId):
    del ids[mId]
    # printAll()
    return


def calculate(sId, eId):

    # 다익스트라의 활용 -> 여러 시작점이 있는 경우
    q = []
    visited = []

    # 초기화
    for i in ids:
        if ids[i][0] <= sId <= ids[i][1] and (sId-ids[i][0]) % ids[i][2] == 0:
            heapq.heappush(q, (0, i))
            visited.append(i)

    # 경로 찾기
    while q:
        now = heapq.heappop(q)
        nowI = now[1]

        # 끝인지 확인
        if ids[nowI][0] <= eId <= ids[nowI][1] and (
                eId - ids[nowI][0]) % ids[nowI][2] == 0:
            return now[0]

        # 끝은 아닌경우 -> 그래프 탐색
        for nextI in graph[nowI]:
            if nextI not in ids or nextI in visited:  # 방문 했으면 스킵
                continue
            # 방문 안한 놈이면
            heapq.heappush(q, (now[0]+1, nextI))
            visited.append(nextI)

    return -1


CMD_INIT = 100
CMD_ADD = 200
CMD_REMOVE = 300
CMD_CALC = 400


def run():
    q = int(sys.stdin.readline())
    okay = False

    mIdArr = []
    sIdArr = []
    eIdArr = []
    mIntervalArr = []

    for i in range(q):
        inputarray = sys.stdin.readline().split()
        cmd = int(inputarray[0])

        if cmd == CMD_INIT:
            inputarray = sys.stdin.readline().split()
            n = int(inputarray[1])
            k = int(inputarray[3])
            for _ in range(k):
                tinfo = sys.stdin.readline().split()
                mIdArr.append(int(tinfo[1]))
                sIdArr.append(int(tinfo[3]))
                eIdArr.append(int(tinfo[5]))
                mIntervalArr.append(int(tinfo[7]))

            init(n, k, mIdArr, sIdArr, eIdArr, mIntervalArr)
            okay = True
        elif cmd == CMD_ADD:
            inputarray = sys.stdin.readline().split()
            mId = int(inputarray[1])
            sId = int(inputarray[3])
            eId = int(inputarray[5])
            mInterval = int(inputarray[7])
            add(mId, sId, eId, mInterval)
        elif cmd == CMD_REMOVE:
            inputarray = sys.stdin.readline().split()
            mId = int(inputarray[1])
            remove(mId)
        elif cmd == CMD_CALC:
            inputarray = sys.stdin.readline().split()
            sId = int(inputarray[1])
            eId = int(inputarray[3])
            ans = int(sys.stdin.readline().split()[1])
            ret = calculate(sId, eId)
            if ans != ret:
                okay = False
        else:
            okay = False

    return okay


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = sys.stdin.readline().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
