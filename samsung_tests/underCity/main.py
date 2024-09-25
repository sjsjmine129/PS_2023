import sys

from collections import defaultdict
import heapq


def printAll():
    print("========================")
    print("<height>")
    print(hights)
    print("\n<door>")
    for i in position:
        print(i)
    print("\n<graph>")
    for i in graph:
        print(i, end=": ")
        for j in graph[i]:
            print(j, end=" ")
        print("")
    print("")


def init(mH: int, mW: int) -> None:
    global h
    global w
    global hights
    global graph
    global position

    h = mH
    w = mW
    hights = [[h, 0, False] for i in range(mW)]
    graph = defaultdict(set)
    position = [{} for i in range(h)]


def dropBox(mId: int, mLen: int, mExitA: int, mExitB: int, mCol: int) -> int:
    # 놓을 수 있는 최대 높이 찾기
    ret = h

    for i in range(mCol, mCol+mLen):
        if hights[i][0] <= ret:
            ret = hights[i][0] - 1

    # 새 건물의 아래 접촉한 부분에 통로가 있으면 간선 추가
    for i in range(mCol, mCol+mLen):
        if hights[i][0] == ret + 1:
            if hights[i][2]:  # 원래꺼 -> 새거
                graph[hights[i][1]].add(mId)
            # 새거 -> 원래거
            if (mExitA == i-mCol or mExitB == i-mCol) and hights[i][1] != 0:
                graph[mId].add(hights[i][1])

        # 건물 최대 높이 업데이트
        if i-mCol == mExitA or i-mCol == mExitB:
            door = True
        else:
            door = False
        hights[i] = [ret, mId, door]

    # 새 건물의 양 옆에 건물이 있으면 간선 서로 추가
    if mCol-1 in position[ret]:  # 왼쪽
        graph[position[ret][mCol-1]].add(mId)
        graph[mId].add(position[ret][mCol-1])
    if mCol+mLen in position[ret]:  # 오른쪽
        graph[position[ret][mCol+mLen]].add(mId)
        graph[mId].add(position[ret][mCol+mLen])

    # 건물의 양옆 정보 기록
    position[ret][mCol] = mId
    position[ret][mCol+mLen-1] = mId

    printAll()

    return ret


def explore(mIdA: int, mIdB: int) -> int:
    exit()
    return -1


CMD_INIT = 1
CMD_DROP = 2
CMD_EXPLORE = 3


def run():
    Q = int(input())
    okay = False

    for q in range(Q):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            mH = int(next(input_iter))
            mW = int(next(input_iter))
            init(mH, mW)
            okay = True
        elif cmd == CMD_DROP:
            mId = int(next(input_iter))
            mLen = int(next(input_iter))
            mExitA = int(next(input_iter))
            mExitB = int(next(input_iter))
            mCol = int(next(input_iter))
            ret = dropBox(mId, mLen, mExitA, mExitB, mCol)
            ans = int(next(input_iter))
            if ret != ans:
                okay = False
        elif cmd == CMD_EXPLORE:
            mIdA = int(next(input_iter))
            mIdB = int(next(input_iter))
            ret = explore(mIdA, mIdB)
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
