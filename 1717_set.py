[n, m] = [int(i) for i in input().split()]


p = [i for i in range(n+1)]


def find(x):
    if (x == p[x]):
        return x

    return find(p[x])


for k in range(m):
    [k, a, b] = [int(i) for i in input().split()]

    if k == 0 and a != b:
        a = find(a)
        b = find(b)
        if a != b:
            if a > b:
                p[b] = a
            else:
                p[a] = b

    elif k == 1:
        if a == b:
            print("YES")
        else:
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
