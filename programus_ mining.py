# *우선순위큐

import heapq


def solution(picks, minerals):
    answer = 0
    dia, iron, stone = picks

    canGet = 5*(dia + iron + stone)
    mineralsNum = len(minerals)
    loopNum = 0

    if mineralsNum >= canGet:
        loopNum = canGet
    else:
        loopNum = mineralsNum

    q = []
    times = 0
    record = []
    for i in range(loopNum):
        now = minerals[i]
        if now == "diamond":
            times += 25
            record.append(25)
        elif now == "iron":
            times += 5
            record.append(5)
        else:
            times += 1
            record.append(1)

        if i % 5 == 4 or i == loopNum-1:  # 마지막 or 5번째
            heapq.heappush(q, (-times, record))
            times = 0
            record = []

    print(q)
    for i in range(len(q)):
        minusSum, data = heapq.heappop(q)
        print(data)
        if dia > 0:
            dia -= 1
            answer += len(data)
        elif iron > 0:
            iron -= 1
            for j in data:
                if j == 25:
                    answer += 5
                else:
                    answer += 1
        else:
            answer += -minusSum

    return answer
