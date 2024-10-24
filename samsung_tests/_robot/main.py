import sys
from typing import List
from collections import defaultdict
from collections import deque


def printAll():
    for i in range(2, 6):
        print("=========================")
        for j in attachShape[i]:
            print(j, ":", attachShape[i][j])


def init(N: int, mMap: List[List[int]]) -> None:
    global island
    global attachShape
    global n

    n = N
    island = []
    attachShape = defaultdict(list)

    for i in range(n):
        island.append([])
        for j in range(n):
            # 지도 저장
            island[i].append(mMap[i][j])
            # 키 저장 -> 가로 세로, 시작은 현재 부터
            Hkey = []
            Vkey = []

            for k in range(1, 5):
                if j+k < n:
                    Hkey.append(mMap[i][j] - mMap[i][j+k])
                    # 현재까지로 키 저장하기
                    key = tuple(Hkey)
                    attachShape[key].append([i, j, 0])
                if i+k < n:
                    Vkey.append(mMap[i][j] - mMap[i+k][j])
                    # 현재까지로 키 저장하기
                    key = tuple(Vkey)
                    attachShape[key].append([i, j, 1])

    # printAll()
    return


# 150,000
def numberOfCandidate(M: int, mStructure: List[int]) -> int:
    ret = 0

    if M == 2:
        key1 = (mStructure[0]-mStructure[1],)
        key2 = (mStructure[1]-mStructure[0],)
    else:
        key1 = tuple(mStructure[index]-mStructure[0] for index in range(1, M))
        key2 = tuple([mStructure[index] - mStructure[-1]
                     for index in range(M - 2, -1, -1)])

    ret = len(attachShape[key1])
    if key1 != key2:
        ret += len(attachShape[key2])

    # print(key1,key2)
    # # print(attachShape[key2])
    print(ret)
    return ret


# 500 -> 설치 가능수는 500 이하
def maxBlockedRobots(M: int, mStructure: List[int], mDir: int) -> int:
    ret = 0

    if M == 2:
        key1 = (mStructure[0]-mStructure[1],)
        key2 = (mStructure[1]-mStructure[0],)
    else:
        key1 = tuple(mStructure[index]-mStructure[0] for index in range(1, M))
        key2 = tuple([mStructure[index] - mStructure[-1]
                     for index in range(M - 2, -1, -1)])

    positionList = attachShape[key1]
    if key1 != key2:
        positionList.extend(attachShape[key2])

    # 각 경우마다 개수 확인
    for position in positionList:
        tempIsland = island
        r = position[0]
        c = position[1]
        dirc = position[2]
        # 설치하기
        if dirc == 0:  # 가로
            if tempIsland[r][c] + mStructure[0] == tempIsland[r][c+1] + mStructure[1]:
                level = tempIsland[r][c] + mStructure[0]
            else:
                level = tempIsland[r][c] + mStructure[M-1]

            for i in range(M):
                tempIsland[r][c+i] = level
        else:  # 세로
            if tempIsland[r][c] + mStructure[0] == tempIsland[r+1][c] + mStructure[1]:
                level = tempIsland[r][c] + mStructure[0]
            else:
                level = tempIsland[r][c] + mStructure[M-1]

            for i in range(M):
                tempIsland[r+i][c] = level

        # 각 곳에서 나가기 만들기
        # for 로 모든 부분에서 여행시작 -> 만약 나갈 수 있는 곳이면 기록해두기(-1) -> 여기 나오면 바로 나올 수 잇는 놈으로 취급
        # 나갈 수 있는 곳 -1, 없는 곳 0, 방문함 -> -2
        # 지나온 곳도 다 체크 시키기

        # 1. 방향에 따라 도착지 -1로 바꾸기
        # 2. for 각 위치로 여행 시작
        # 3. 현재보다 작으면 이동 -> 방문함 리스트에 기록
        # 4. -1 만나면 break하고 방문함 리스트에 구역 다 -1로 바꾸기 & 개수 기록
        # 5. 결국 도착 못하면 방문함 리스트에 구역 다 0만들기

    # print(ret)
    return ret

##############################################################################


CMD_INIT = 100
CMD_CANDI = 200
CMD_BLOCKED = 300


def run():
    query = int(input())
    ok = False
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            mMap = []
            for j in range(N):
                input_iter = iter(input().split())
                row = [int(val) for val in input_iter]
                mMap.append(row)
            init(N, mMap)
            ok = True
        elif cmd == CMD_CANDI:
            M = int(next(input_iter))
            mStructure = []
            for j in range(M):
                mStructure.append(int(next(input_iter)))
            ret = numberOfCandidate(M, mStructure)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
        elif cmd == CMD_BLOCKED:
            M = int(next(input_iter))
            mStructure = []
            for j in range(M):
                mStructure.append(int(next(input_iter)))
            mDir = int(next(input_iter))
            ret = maxBlockedRobots(M, mStructure, mDir)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
    return ok


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
