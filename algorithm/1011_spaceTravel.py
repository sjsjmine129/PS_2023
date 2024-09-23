import math

n = int(input())

for k in range(n):
    [A, B] = input().split()
    A = int(A)
    B = int(B)

    gap = B - A

    n = 0.1
    x = 0

    while n % 1 != 0:
        # print(n, x)
        n = (math.sqrt(1+4*(gap-x))-1)/2
        x += 1

    n = int(n)

    if x == 1:
        answer = 2*n
    elif x-1 > n+1:
        answer = 2*n+2
    else:
        answer = 2*n+1

    print(answer)
