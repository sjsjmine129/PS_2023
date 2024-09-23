# memory is full

from itertools import combinations

[m, n] = map(int, input().split())

lamp = []

for i in range(m):
    temp = []
    for j in input():
        if j == "0":
            temp.append(False)
        else:
            temp.append(True)
    lamp.append(temp)

k = int(input())


def countLight(changeList):
    count = 0
    for i in lamp:
        checker = True
        for j in range(len(i)):
            if j in changeList:
                if i[j]:
                    checker = False
                    break
            elif i[j] == False:
                checker = False
                break
        if checker:
            count += 1
    return count


maxNum = 0

start = k % 2
while start <= n and start <= k:
    for j in list(combinations(range(n), start)):
        maxNum = max(maxNum, countLight(j))
    start += 2

print(maxNum)
