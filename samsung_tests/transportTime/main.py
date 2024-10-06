import sys
from typing import List
from collections import defaultdict
import heapq
INF = int(1e9)


def printAll():
    printGlobal()
    printGroup()


def printGlobal():
    for i in globalGraph:
        print(i, ": ", globalGraph[i])


def printGroup():
    for i in range(1, n+1):
        print(i, "==============")
        for j in groupGraph[i]:
            print(i*100+j, ":", groupGraph[i][j])


def init(N: int, K: int, mNodeA: List[int], mNodeB: List[int], mTime: List[int]) -> None:
    global globalGraph
    global groupGraph
    global recordDistance
    global changed
    global n
    global k

    k = K
    n = N

    changed = [True, True, True]
    recordDistance = [0, 0, 0]  # 1-2, 1-3, 2-3
    groupGraph = [defaultdict(dict) for _ in range(n+1)]
    globalGraph = defaultdict(dict)

    for i in range(k):
        nodeA = mNodeA[i]
        nodeB = mNodeB[i]
        time = mTime[i]
        if nodeA <= 3 or nodeB <= 3:  # 루트 노드의 간선
            globalGraph[nodeA][nodeB] = time
            globalGraph[nodeB][nodeA] = time
        else:  # 내부 노드들의 간선
            addLine(nodeA, nodeB, time)

    # printAll()


def resetGroupDistance(group):
    nowGraph = groupGraph[group]  # dic

    # 각 node에서 서로로 가는 루트 드는 시간 찾기
    # node 1에서 2,3가는거 찾기
    q = []
    distance = [INF for _ in range(31)]
    distance[1] = 0

    heapq.heappush(q, (0, 1))

    while q:
        now = heapq.heappop(q)

        # 이미 갱신 된거면 스킵
        if distance[now[1]] < now[0]:
            continue

        for nextNode in nowGraph[now[1]]:
            if distance[nextNode] > now[0] + nowGraph[now[1]][nextNode]:
                distance[nextNode] = now[0] + nowGraph[now[1]][nextNode]
                heapq.heappush(q, (distance[nextNode], nextNode))

    # record Data
    globalGraph[group*100 + 1][group*100 + 2] = distance[2]
    globalGraph[group*100 + 2][group*100 + 1] = distance[2]
    globalGraph[group*100 + 1][group*100 + 3] = distance[3]
    globalGraph[group*100 + 3][group*100 + 1] = distance[3]

    # node 2에서 3가는거 찾기
    q = []
    distance = [INF for _ in range(31)]
    distance[2] = 0

    heapq.heappush(q, (0, 2))

    while q:
        now = heapq.heappop(q)

        # 이미 갱신 된거면 스킵
        if distance[now[1]] < now[0]:
            continue

        for nextNode in nowGraph[now[1]]:
            if distance[nextNode] > now[0] + nowGraph[now[1]][nextNode]:
                distance[nextNode] = now[0] + nowGraph[now[1]][nextNode]
                heapq.heappush(q, (distance[nextNode], nextNode))

    # record Data
    globalGraph[group*100 + 3][group*100 + 2] = distance[3]
    globalGraph[group*100 + 2][group*100 + 3] = distance[3]


def addLine(mNodeA: int, mNodeB: int, mTime: int) -> None:
    global changed
    idA = mNodeA % 100
    groupA = mNodeA//100
    idB = mNodeB % 100
    groupB = mNodeB//100

    if groupA == groupB:  # 동일 그룹 내 간선
        group = groupA
        # 그룹 내부 그래프 수정
        groupGraph[group][idA][idB] = mTime
        groupGraph[group][idB][idA] = mTime

        # 그룹 내부 3개끼리의 거리 계산
        resetGroupDistance(group)
        # printGroup()
        # exit()
    else:  # 다른 그룹간의 간선
        globalGraph[mNodeA][mNodeB] = mTime
        globalGraph[mNodeB][mNodeA] = mTime

    changed = [True, True, True]


def removeLine(mNodeA: int, mNodeB: int) -> None:
    global changed
    idA = mNodeA % 100
    groupA = mNodeA//100
    idB = mNodeB % 100
    groupB = mNodeB//100

    if groupA == groupB:  # 동일 그룹 내 간선
        group = groupA
        # 그룹 내부 그래프 수정
        if idA in groupGraph[group] and idB in groupGraph[group][idA]:
            # print(groupGraph[group][idA])
            del groupGraph[group][idA][idB]
            del groupGraph[group][idB][idA]
            # print(groupGraph[group][idA])

        # 그룹 내부 3개끼리의 거리 계산
        resetGroupDistance(group)

        # print(groupGraph)
        # printGroup()
        # exit()
    else:  # 다른 그룹간의 간선
        del globalGraph[mNodeA][mNodeB]
        del globalGraph[mNodeB][mNodeA]

    changed = [True, True, True]


def checkDistance(which):  # 0이면 1-2거리 갱신 필요, 1이면 1-3, 2면 2-3
    global changed
    if which == 0 or which == 1:  # 1의 거리 계산
        q = []
        distance = {}
        for i in globalGraph:
            distance[i] = INF

        distance[1] = 0
        heapq.heappush(q, (0, 1))

        while q:
            now = heapq.heappop(q)
            if distance[now[1]] < now[0]:
                continue

            for nextNode in globalGraph[now[1]]:
                if distance[nextNode] > now[0] + globalGraph[now[1]][nextNode]:
                    distance[nextNode] = now[0] + globalGraph[now[1]][nextNode]
                    heapq.heappush(q, (distance[nextNode], nextNode))

        recordDistance[0] = distance[2]
        recordDistance[1] = distance[3]
        changed[0] = False
        changed[1] = False

    else:  # 2의 거리 계산
        q = []
        distance = {}
        for i in globalGraph:
            distance[i] = INF

        distance[2] = 0
        heapq.heappush(q, (0, 2))

        while q:
            now = heapq.heappop(q)
            if distance[now[1]] < now[0]:
                continue

            for nextNode in globalGraph[now[1]]:
                if distance[nextNode] > now[0] + globalGraph[now[1]][nextNode]:
                    distance[nextNode] = now[0] + globalGraph[now[1]][nextNode]
                    heapq.heappush(q, (distance[nextNode], nextNode))

        recordDistance[0] = distance[1]
        recordDistance[2] = distance[3]
        changed[0] = False
        changed[2] = False


def checkTime(mNodeA: int, mNodeB: int) -> int:

    if (mNodeA == 1 and mNodeB == 2) or (mNodeA == 2 and mNodeB == 1):
        if changed[0]:
            checkDistance(0)
        ret = recordDistance[0]
    elif (mNodeA == 1 and mNodeB == 3) or (mNodeA == 3 and mNodeB == 1):
        if changed[1]:
            checkDistance(1)
        ret = recordDistance[1]
    else:
        if changed[2]:
            checkDistance(2)
        ret = recordDistance[2]

    # print(ret)
    return ret

########################################################################################################################################################################


CMD_INIT = 0
CMD_ADD = 1
CMD_REMOVE = 2
CMD_CHECK = 3

MAX_LINE = 30000

nodeA = [0 for _ in range(MAX_LINE)]
nodeB = [0 for _ in range(MAX_LINE)]
Time = [0 for _ in range(MAX_LINE)]


def run():
    input_iter = iter(input().split())
    Q = int(next(input_iter))
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            K = int(next(input_iter))
            for i in range(0, K):
                input_iter = iter(input().split())
                nodeA[i] = int(next(input_iter))
                nodeB[i] = int(next(input_iter))
                Time[i] = int(next(input_iter))
            init(N, K, nodeA, nodeB, Time)
            okay = True
        elif cmd == CMD_ADD:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            time = int(next(input_iter))
            addLine(node_a, node_b, time)
        elif cmd == CMD_REMOVE:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            removeLine(node_a, node_b)
        elif cmd == CMD_CHECK:
            node_a = int(next(input_iter))
            node_b = int(next(input_iter))
            ret = checkTime(node_a, node_b)
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
