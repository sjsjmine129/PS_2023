# *graph
# *loop
# *dfs


t = int(input())
for times in range(t):
    n = int(input())
    choose = [int(i) for i in input().split()]

    ret = 0

    for i in range(len(choose)):
        if choose[i] == -1:
            continue

        check = []

        check.append(i+1)
        nextNode = choose[i]
        choose[i] = -1

        while True:
            if nextNode == -1:  # Loop 찾은 경우 & 끊긴경우
                loop = 0
                start = check[-1]
                for j in range(len(check)):
                    if check[j] == start and j != len(check):
                        break
                    ret += 1
                break
            else:
                check.append(nextNode)
                temp = nextNode - 1
                nextNode = choose[nextNode-1]
                choose[temp] = -1

    print(ret)
