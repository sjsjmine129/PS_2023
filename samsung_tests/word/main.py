import sys


def printWord():
    for i in paperData:
        print(i)


class Node:
    def __init__(self, value):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value


class LeafNode:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.row = 0


def makeTree(start, end, parent, left):
    # 마지막 노드 일때
    if start == end:
        new = LeafNode(m)
        new.parent = parent
        new.row = start
        if left:
            parent.left = new
        else:
            parent.right = new
        ##
        leafNodeList[start] = new
    else:  # 중간 노드일 때
        new = Node(m)
        new.parent = parent
        if left:
            parent.left = new
        else:
            parent.right = new

        mid = (start + end) // 2
        makeTree(start, mid, new, True)
        makeTree(mid+1, end, new, False)


def travelTree(nowNode, value) -> LeafNode:
    # 끝 도달시
    if type(nowNode) == LeafNode:
        return nowNode

    if nowNode.left.value >= value:
        return travelTree(nowNode.left, value)
    elif nowNode.right.value >= value:
        return travelTree(nowNode.right, value)
    else:
        return LeafNode(-1)


def recoredNewEmpty(row):
    # 빈칸 찾기
    maxLen = 0
    tempLen = 0
    for i in paperData[row]:
        if i == 0:
            tempLen += 1
            if tempLen > maxLen:
                maxLen = tempLen
        else:
            tempLen = 0

    # 트리 업데이트
    leafNodeList[row].value = maxLen

    nowNode = leafNodeList[row].parent

    while nowNode.parent != None:  # 루트까지
        childMax = max(nowNode.left.value, nowNode.right.value)
        if nowNode.value != childMax:  # 바뀜
            nowNode.value = childMax
            nowNode = nowNode.parent
        else:  # 그대로
            break


def init(N: int, M: int) -> None:
    global wordData
    global root
    global paperData
    global leafNodeList
    global n
    global m
    n = N
    m = M
    leafNodeList = [None]*n

    # 단어장 기록
    paperData = [[0]*m for _ in range(n)]

    # 단어들    [열, 행, 길이]
    wordData = {}

    # 길이 테스트용
    # wordMax = 50000
    # for i in range(wordMax):
    #     wordData[i] = [1, 1, 1]

    # 최대 빈공간 트리 만들기
    root = Node(m)
    mid = n//2
    makeTree(0, mid, root, True)
    makeTree(mid + 1, n-1, root, False)


def writeWord(mId: int, mLen: int) -> int:
    findNode = travelTree(root, mLen)

    if findNode.value == -1:  # 들어갈 데 없음
        # print(-1)
        return -1

    # 기록 가능 행 찾기
    tempLen = 0
    colunm = -1  # 무조건 있음 -> 실제 기록위치
    before = 1
    for i in range(m):
        tempId = paperData[findNode.row][i]
        if before == 1 and tempId == 0:  # 빈칸의 시작
            colunm = i
            tempLen = 1
            before = 0
        elif tempId == 0:  # 빈칸 세는중에 또 빈칸
            tempLen += 1
        else:  # 막힘
            before = 1
            tempLen = 0
            continue

        # 빈칸이 더 긴지
        if tempLen == mLen:
            break

    # 기록 시작
    # 단어장 기록
    for i in range(mLen):
        paperData[findNode.row][colunm + i] = mId
    # 단어 정보 기록
    wordData[mId] = [findNode.row, colunm, mLen]
    # 공백 기록
    recoredNewEmpty(findNode.row)

    # print(findNode.row)
    # printWord()
    return findNode.row


def eraseWord(mId: int) -> int:
    if mId not in wordData:  # 없음
        # print(-1)
        return -1

    ret = wordData[mId][0]

    # 단어장에서 지우기
    for i in range(wordData[mId][2]):
        paperData[wordData[mId][0]][wordData[mId][1]+i] = 0

    # 트리 갱신
    recoredNewEmpty(wordData[mId][0])

    # 단어 데이터 지우기
    del wordData[mId]

    # print(ret)
    return ret


##############################################################################################################################

CMD_INIT = 1
CMD_WRITE = 2
CMD_ERASE = 3


def run():
    query = int(input())
    ok = False
    for i in range(query):
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            N = int(next(input_iter))
            M = int(next(input_iter))
            init(N, M)
            ok = True
        elif cmd == CMD_WRITE:
            mId = int(next(input_iter))
            mLen = int(next(input_iter))
            ret = writeWord(mId, mLen)
            ans = int(next(input_iter))
            if ans != ret:
                ok = False
        elif cmd == CMD_ERASE:
            mId = int(next(input_iter))
            ret = eraseWord(mId)
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
