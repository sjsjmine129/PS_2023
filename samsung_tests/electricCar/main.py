import sys
from typing import List
from collections import defaultdict
from collections import deque
import heapq


def init(N: int, mRange: int, mMap: List[List[int]]) -> None:
    global city
    global charge
    global n
    global graph
    global stationNum

    n = N
    city = [[mMap[i][j]-2 for j in range(n)] for i in range(n)]
    charge = mRange
    graph = defaultdict(list)
    stationNum = 0

    return


dirction = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def add(mID: int, mRow: int, mCol: int) -> None:
    global stationNum

    city[mRow][mCol] = mID
    stationNum += 1

    q = deque([])
    visited = [[False]*n for _ in range(n)]
    visited[mRow][mCol] = True
    q.append([0, mRow, mCol])

    while q:
        now = q.popleft()
        if now[0] == charge:  # 충전소의 범위까지만
            continue

        for dirc in dirction:
            nextR = now[1] + dirc[0]
            nextC = now[2] + dirc[1]
            if 0 <= nextR < n and 0 <= nextC < n and not visited[nextR][nextC]:
                if city[nextR][nextC] == -2:  # 빈칸
                    visited[nextR][nextC] = True
                    q.append([now[0]+1, nextR, nextC])
                elif city[nextR][nextC] != -1:  # 충전소
                    visited[nextR][nextC] = True
                    graph[mID].append([now[0]+1, city[nextR][nextC]])
                    graph[city[nextR][nextC]].append([now[0]+1, mID])

    # printAll()
    return


def distance(mFrom: int, mTo: int) -> int:
    # print(stationNum)

    far = [122501 for _ in range(stationNum)]
    far[mFrom] = 0

    q = []
    heapq.heappush(q, [0, mFrom])

    while q:
        now = heapq.heappop(q)
        if far[now[1]] < now[0]:  # 이미 갱신 된놈이면 스킵
            continue

        if now[1] == mTo:  # 최소인데 도착했으면 끝
            ret = now[0]
            break

        for nextStaion in graph[now[1]]:
            if far[nextStaion[1]] > now[0] + nextStaion[0]:
                far[nextStaion[1]] = now[0] + nextStaion[0]
                heapq.heappush(q, [now[0]+nextStaion[0], nextStaion[1]])

    ret = far[mTo]
    if ret == 122501:
        ret = -1
    return ret

############################################################


CMD_INIT = 0
CMD_ADD = 1
CMD_DISTANCE = 2


def run():
    len = int(sys.stdin.readline())

    for i in range(len):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            Range = int(next(inputs))
            map = []
            for j in range(N):
                inputs2 = iter(sys.stdin.readline().split())
                row = [int(val) for val in inputs2]
                map.append(row)
            init(N, Range, map)
            ret_val = 1

        elif cmd == CMD_ADD:
            id = int(next(inputs))
            r = int(next(inputs))
            c = int(next(inputs))
            ret = add(id, r, c)

        elif cmd == CMD_DISTANCE:
            id = int(next(inputs))
            id2 = int(next(inputs))
            ret = distance(id, id2)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

    return ret_val


if __name__ == '__main__':
    sys.stdin = open('sample_input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
