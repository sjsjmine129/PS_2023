n = int(input())

numbers = [[] for i in range(n)]

for i in range(5):
    line = input()

    index = 0
    k = 0
    for j in line:
        if index != 3 and j == "#":
            numbers[k].append((i*3)+index)

        index += 1
        if index == 4:
            index = 0
            k += 1

# for i in numbers:
#     print(i)

able = [[8] for i in range(n)]

for i in range(n):
    light = numbers[i]
    record = able[i]

    if 4 in light or 10 in light:
        print(-1)
        exit()

    if 7 not in light:
        record.append(0)
        if all(num not in light for num in [3, 6, 9, 12, 13]):
            record.append(7)
            if all(num not in light for num in [0, 1]):
                record.append(1)

    if 5 not in light:
        record.append(6)
        if 9 not in light:
            record.append(5)

    if all(num not in light for num in [9]):
        record.append(9)
        if all(num not in light for num in [1, 12, 13]):
            record.append(4)

    if all(num not in light for num in [3, 11]):
        record.append(2)

    if all(num not in light for num in [3, 9]):
        record.append(3)

ret = 0
times = 0
for i in reversed(able):
    sumAll = sum(i)
    ret += (sumAll*(10**times))/len(i)
    times += 1

print(ret)
