# *재귀
# *dp

import sys
sys.setrecursionlimit(10**6)


def solution(sequence):
    lenSeq = len(sequence)
    answer = sequence[0]

    def findMax(startIndex):
        nonlocal answer
        now1 = sequence[startIndex]
        now2 = -sequence[startIndex]
        if startIndex % 2 == 1:
            now1 = -now1
            now2 = -now2

        if startIndex == lenSeq - 1:
            if answer < now1:
                answer = now1
            if answer < now2:
                answer = now2
            return (now1, now2)
        else:
            nextFind = findMax(startIndex + 1)
            max1 = max(now1, now1+nextFind[0])
            max2 = max(now2, now2+nextFind[1])
            if answer < max1:
                answer = max1
            if answer < max2:
                answer = max2
            return (max1, max2)

    findMax(0)

    return answer
