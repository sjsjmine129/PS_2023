# n개의 벨트를 설치하고, 총 m개의 물건

#  벨트 리스트 [(맨앞놈, 맨뒷놈, 길이, 중간놈?)  ]
#  선물 리스트 [(앞놈: 없으면 -1, 뒷놈),()....]

from math import floor

q = int(input())

belt = []
present = []
n = 0
m = 0
length = 2
front = 0
back = 1

# 벨트, 선물 현황 그리기


def printAll():
    for index in range(1, len(belt)):
        i = belt[index]
        print("belt", index, "===========")
        print("first:", i[front])
        print("last:", i[back])
        print("length:", i[length])
        node = i[front]
        while node != -1:
            print(node, end=" ")
            node = present[node][back]
        print("")
        node = i[back]
        while node != -1:
            print(node, end=" ")
            node = present[node][front]
        print("")


# 공장 설림
def buildFac(inputList):
    # 데이터 입력
    for newP in range(1, len(inputList)-2):
        nowBelt = inputList[newP+2]
        # 빈 벨트의 경우
        if belt[nowBelt][length] == 0:
            # 벨트 정보 갱신
            belt[nowBelt][front] = newP
            belt[nowBelt][back] = newP
            belt[nowBelt][length] = 1

        # 벨트에 다른 것이 있는 경우
        else:
            beLast = belt[nowBelt][back]
            # 선물 정보 갱신
            present[beLast][back] = newP  # 전놈 뒤에 이번꺼
            present[newP][front] = beLast  # 이번꺼 앞에 전 마지막

            # 벨트 정보 갱신
            belt[nowBelt][back] = newP
            belt[nowBelt][length] = belt[nowBelt][length] + 1


# 물건 모두 옮기기
def moveAll(src, dst):
    if belt[src][length] == 0:
        print(belt[dst][length])
        return

    # 박스들의 위치 바꾸기
    present[belt[dst][front]][front] = belt[src][back]  # dst의 맨 앞놈 앞
    present[belt[src][back]][back] = belt[dst][front]  # src의 맨 뒤놈 뒤

    # dst 벨트 정보 바꾸기
    lenBefore = belt[dst][length]
    lenAdd = belt[src][length]
    belt[dst][length] = lenBefore + lenAdd  # 개수 늘리기
    belt[dst][front] = belt[src][front]  # 맨 앞놈 지정

    # 마지막놈 바꾸기
    if lenBefore == 0:
        belt[dst][back] = belt[src][back]
    # #길이가 0이면 마지막놈 바꾸기
    if belt[dst][length] == 1:
        belt[dst][back] = belt[dst][front]

    # src 벨트 정보 바꾸기
    belt[src] = [-1, -1, 0, -1]

    # print
    print(belt[dst][length])


# 앞 물건 옮기기
def changeFront(src, dst):
    srcFront = belt[src][front]
    dstFront = belt[dst][front]

    if srcFront == -1 and dstFront == -1:  # 둘다 빔
        print(belt[dst][length])
        return
    elif srcFront == -1:  # src만 빔
        # 안빈놈 벨트 정보 수정
        belt[dst][front] = present[dstFront][back]  # 두번째놈 맨앞으로
        present[belt[dst][front]][front] = -1
        belt[dst][length] = belt[dst][length] - 1  # 길이 감소
        if belt[dst][length] == 0:  # 만약 다 비워지면 뒤도 삭제
            belt[dst][back] = -1

        # 이동한 선물 정보 수정
        present[dstFront][back] = -1

        # 원래 비엇던 벨트 정보 수정
        belt[src] = [dstFront, dstFront, 1, dstFront]

    elif dstFront == -1:  # dst만 빔
        # 안빈놈 벨트 정보 수정
        belt[src][front] = present[srcFront][back]  # 두번째놈 맨앞으로
        present[belt[src][front]][front] = -1
        belt[src][length] = belt[src][length] - 1  # 길이 감소
        if belt[src][length] == 0:  # 만약 다 비워지면 뒤도 삭제
            belt[src][back] = -1

        # 이동한 선물 정보 수정
        present[srcFront][back] = -1

        # 원래 비엇던 벨트 정보 수정
        belt[dst] = [srcFront, srcFront, 1, srcFront]

    else:  # 둘 다 있음
        # 맨 앞의 두놈의 뒤 교체
        temp = present[srcFront][back]
        present[srcFront][back] = present[dstFront][back]
        present[dstFront][back] = temp

        present[present[srcFront][back]][front] = srcFront
        present[present[dstFront][back]][front] = dstFront

        # 벨트 정보 수정
        belt[src][front] = dstFront
        belt[dst][front] = srcFront
        if belt[src][length] == 1:
            belt[src][back] = dstFront

        if belt[dst][length] == 1:
            belt[dst][back] = srcFront

    print(belt[dst][length])


# 물건 나누기
def splitPresent(src, dst):
    srcLen = belt[src][length]
    if srcLen <= 1:  # 1 이하면 종료
        print(belt[dst][length])
        return

    halfSrcLen = floor(srcLen/2)
    srcFront = belt[src][front]
    srcMiddle = belt[src][front]
    for i in range(halfSrcLen - 1):  # 중간놈 찾기
        srcMiddle = present[srcMiddle][back]

    # src벨트 수정
    belt[src][front] = present[srcMiddle][back]  # 맨 앞 중간의 뒤
    present[belt[src][front]][front] = -1  # 그 선물의 앞 지우기
    belt[src][length] = srcLen - halfSrcLen  # 길이 감소
    present[srcMiddle][back] = -1  # 중간놈의 뒤 삭제

    # dst 벨트 수정
    if belt[dst][length] == 0:  # 빈 곳으로 보낼때
        belt[dst] = [srcFront, srcMiddle, halfSrcLen]
    else:  # 있는 곳으로 보낼 때
        present[srcMiddle][back] = belt[dst][front]  # 기존 맨앞 선물을 middle의 뒷놈
        present[belt[dst][front]][front] = srcMiddle  # 기존 맨앞 선물의 앞을 middle로

        belt[dst][front] = srcFront
        belt[dst][length] = belt[dst][length] + halfSrcLen

    print(belt[dst][length])


# 선물정보 얻기
def getPresent(pId):
    a = present[pId][front]
    b = present[pId][back]

    print(a+2*b)

# 선물정보 얻기


def getBelt(bId):
    a = belt[bId][front]
    b = belt[bId][back]
    c = belt[bId][length]

    print(a + 2*b + 3*c)

######################## 작동부 ###################


for time in range(q):
    inputL = [int(i) for i in input().split()]
    # print(time,"=======")

    if inputL[0] == 100:
        n = inputL[1]
        m = inputL[2]

        belt = [[-1, -1, 0] for _ in range(n+1)]
        present = [[-1, -1] for _ in range(m+2)]

        buildFac(inputL)
        # printAll()

    elif inputL[0] == 200:
        moveAll(inputL[1], inputL[2])
        # printAll()

    elif inputL[0] == 300:
        changeFront(inputL[1], inputL[2])
        # printAll()

    elif inputL[0] == 400:
        splitPresent(inputL[1], inputL[2])
        # printAll()

    elif inputL[0] == 500:
        getPresent(inputL[1])
        # printAll()

    elif inputL[0] == 600:
        getBelt(inputL[1])
        # printAll()
