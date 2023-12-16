import sys
max_integer = sys.maxsize

[v, e] = [int(i) for i in input().split()]
start = int(input())

edge = {}
for i in range(v+1):
    edge[i] = []
for i in range(e):
    temp = input().split()
    a = edge[int(temp[0])]
    a.append([int(temp[1]), int(temp[2])])
    edge[temp[0]] = a


ret = [max_integer for i in range(v+1)]
ret[start] = 0
q = [max_integer for i in range(v+1)]
q[start] = 0

s = []

while len(s) != v:
    min_value = min(q)
    min_index = q.index(min_value)

    if min_value == max_integer:
        break

    for go in edge[min_index]:
        if ret[go[0]] > min_value + go[1]:
            ret[go[0]] = min_value + go[1]
            q[go[0]] = min_value + go[1]

    s.append(min_index)
    q[min_index] = max_integer

# print(ret)
# print(q)
# print(s)
for i in range(1, v+1):
    if ret[i] == max_integer:
        print('INF')
    else:
        print(ret[i])
