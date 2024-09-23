
T = int(input())


def checkCase(case):
    [a, b, c] = map(int, input().split())

    if c < 3 or b < 2:
        print("#", end='')
        print(case, end=' ')
        print(-1)
        return

    eat = 0

    if c <= b:
        eat = b - c + 1
        b = b - eat

    if b <= a:
        tempEat = a - b + 1
        a = a - tempEat
        eat += tempEat

    print("#", end='')
    print(case, end=' ')
    print(eat)


for case in range(1, T + 1):
    checkCase(case)
