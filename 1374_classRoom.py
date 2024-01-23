n = int(input())

list = []

for i in range(n):
    [a, b, c] = input().split()
    list.append([int(a), int(b), int(c)])

# sort with second and third one
list = sorted(list, key=lambda x: (x[1], x[2]))

q = []
q.append(list.pop(0)[2])

# print(q)
for i in list:
    if i[1] < q[0]:
        checker = True
        for j in range(len(q)):
            if i[2] <= q[j]:
                q.insert(j, i[2])
                checker = False
                break
        if checker:
            q.append(i[2])
    else:
        q.pop(0)
        checker = True
        for j in range(len(q)):
            if i[2] <= q[j]:
                q.insert(j, i[2])
                checker = False
                break
        if checker:
            q.append(i[2])

print(len(q))
