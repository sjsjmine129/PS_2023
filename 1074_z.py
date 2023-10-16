N, r, c = map(int, input().split())

now = 2**(N-1)

answer = 0

while now > 0:

    if r < now and c >= now:
        answer = answer + now**2
        c = c - now
    elif r >= now and c < now:
        answer = answer + 2*(now**2)
        r = r-now
    elif r >= now and c >= now:
        answer = answer + 3*(now**2)
        r = r-now
        c = c-now

    now = now//2


print(answer)
