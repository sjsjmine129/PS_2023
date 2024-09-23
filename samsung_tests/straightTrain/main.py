from itertools import combinations
import sys


def printAll():
    for i in graph:
        print(i)
    print("")
    for i in ids:
        print("<", i, ">")
        for j in ids[i]:
            print(j, end=" ")
        print("")


# 열차의 데이터를 받아서 에지를 리턴
def getEdges(start, end, inter):
    edges = []

    for i in range(start, end+1, inter):
        for j in range(i + inter, end + 1, inter):
            edges.append([i, j])

    return edges


def init(N, K, mId, sId, eId, mInterval):
    global n
    global k
    global graph
    global ids
    n = N
    k = K
    ids = {}

    graph = [{} for _ in range(n+1)]

    for i in range(k):
        #
        ids[mId[i]] = (sId[i], eId[i], mInterval[i])
        edges = getEdges(sId[i], eId[i], mInterval[i])

        for edge in edges:
            if edge[1] in graph[edge[0]]:
                temp = graph[edge[0]][edge[1]]
                graph[edge[0]][edge[1]] = temp + 1
                graph[edge[1]][edge[0]] = temp + 1
            else:
                graph[edge[0]][edge[1]] = 1
                graph[edge[1]][edge[0]] = 1
    printAll()
    return


def add(mId, sId, eId, mInterval):
    return


def remove(mId):
    return


def calculate(sId, eId):
    return 0


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
