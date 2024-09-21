INF = int(1e9)
q = [-1]


def heappush(a):
    q.append(a)

    index = len(q)-1
    now = a

    while index != 1:
        pIndex = index//2
        parent = q[pIndex]

        if parent > now:
            q[index] = parent
            index = pIndex
            q[index] = a
        else:
            break


def heappop():
    ret = q[1]

    index = 1
    q[1] = q[len(q)-1]
    q.pop()

    while index < len(q):
        now = q[index]
        if index*2 < len(q):
            left = q[index*2]
        else:
            left = INF
        if index*2 + 1 < len(q):
            right = q[index*2 + 1]
        else:
            right = INF

        if left <= right:
            nextI = index*2
            son = left
        else:
            nextI = index*2 + 1
            son = right

        if now > right:
            q[index] = son
            q[nextI] = now
            index = nextI
        else:
            break

    return ret


heappush(3)
heappush(5)
heappush(2)
heappush(1)
heappush(6)
heappush(-2)

print(q)
print(heappop())
print(q)
print(heappop())
print(q)
print(heappop())
print(q)
