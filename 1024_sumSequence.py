import math

temp = input().split()
[N, L] = [int(x) for x in temp]


if (L % 2 == 0):
    fib = int((L+1)*(L/2) - L)
else:
    fib = int((L+1)*(L-1)/2 + (L+1)/2 - L)


for i in range(L, 101):
    if (N-fib) < 0:
        x = -1
        break
    elif (N-fib) % i == 0:
        x = int((N-fib)/i)
        break
    else:
        fib += i
        x = -1

if (x == -1):
    print(x)
    exit()

for k in range(0, i):
    if (k == i-1):
        print(x+k)
    else:
        print(x+k, end=' ')
