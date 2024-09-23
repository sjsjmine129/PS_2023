n = int(input())

for j in range(n):
    [x1, y1, r1, x2, y2, r2] = map(int, input().split())

    if x1 == x2 and y1 == y2:
        if r1 != r2:
            print(0)
            continue
        else:
            print(-1)
            continue

    len = (((x1-x2)**2)+((y1-y2)**2))**0.5

    if r1 < r2:
        temp = r1
        r1 = r2
        r2 = temp

    if (r1+r2) == len or (r1-r2) == len:
        print(1)
    elif (r1+r2) < len or (r1-r2) > len:
        print(0)
    else:
        print(2)
