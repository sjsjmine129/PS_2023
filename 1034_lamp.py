# memory is full

from itertools import combinations

[m, n] = map(int, input().split())

lamp = []

for i in range(m):
    temp = []
    count = 0
    for j in input():
        if j == "0":
            temp.append(False)
            count += 1
        else:
            temp.append(True)
    temp.append(count)
    lamp.append(temp)
# print(lamp)
k = int(input())
Ktype = k % 2

maxNum = 0

for i in lamp:
    if i[-1] % 2 == Ktype and i[-1] <= k:
        same = 0
        for j in lamp:
            if j == i:
                same += 1
        if maxNum < same:
            maxNum = same
print(maxNum)
