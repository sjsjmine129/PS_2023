# *queue

from collections import deque


def solution(sequence, k):
    answer = []
    minlen = len(sequence)
    start = 0
    end = 0
    temp = deque()
    sum = 0

    for i in range(len(sequence)):
        now = sequence[i]
        sum += now
        temp.append(now)
        end = i

        while sum > k:
            sum -= temp.popleft()
            start += 1

        if sum == k and end - start < minlen:
            print(minlen)
            minlen = end - start
            answer = [start, end]

    return answer
