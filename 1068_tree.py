n = int(input())

temp = input().split()
list = [int(x) for x in temp]

k = int(input())

delete = []
delete.append(k)
list[k] = -2

while len(delete) != 0:
    index = delete.pop()

    for i in range(0, n):
        if list[i] == index:
            delete.append(i)
            list[i] = -2

answer = 0

for i in range(0, n):
    if list[i] != -2:
        checker = 0

        for j in range(0, n):
            if list[j] == i:
                checker = 1

        if checker == 0:
            answer = answer + 1


print(answer)
