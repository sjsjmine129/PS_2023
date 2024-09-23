import math

length = int(input())

temp = input().split()
a = [int(x) for x in temp]


b = a.copy()
b.sort()

tmep = []

for i in range(length):
    for j in range(length):
        if a[i] == b[j]:
            temp[i] = j
            b[j] = -1
            break

for i in temp:
    print(i, end=' ')
