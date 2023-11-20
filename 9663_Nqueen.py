N = int(input())

num = 0


def dfs(ylist):
    global num
    x = len(ylist)

    # 되는 경우
    if x == N:
        num += 1
    else:
        for y in range(N):
            dif = x-y
            sum = x+y

            cheker = 0
            for i in range(len(ylist)):
                if y == ylist[i] or dif == i-ylist[i] or sum == i+ylist[i]:
                    cheker = 1
                    break

            if cheker == 0:
                dfs((lambda lst: lst + [y])(ylist))


dfs([])

print(num)
