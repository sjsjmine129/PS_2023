def solution(edges):

    sorce = 0

    sorted_list = sorted(edges, key=lambda x: x[1])
    # print(sorted_list)
    # 시작점 찾기
    now = 0
    check = False
    for i in sorted_list:
        if now != i[1]:
            if now+1 == i[1]:
                now = i[1]
            else:
                sorce = now+1
                check = True
                break
    if check == False:
        sorce = sorted_list[-1][1]+1

    start_edge = []
    togo = [0 for i in range(1000000+3)]

    for i in edges:

        if i[0] == sorce:
            start_edge.append(i)

        from_v = i[0]
        to_v = i[1]
        if togo[from_v] == 0:  # 처음
            togo[from_v] = to_v
        elif togo[from_v] > 0:  # 처음 아닌경우
            togo[from_v] = -1

    donut = 0
    stick = 0
    s_8 = 0

    for i in start_edge:
        visit = []
        go = i[1]

        while True:
            visit.append(go)
            if togo[go] == -1:    # 두개
                s_8 += 1
                break
            elif togo[go] == 0:  # 끝
                stick += 1
                break
            elif togo[go] in visit:  # 사이클
                if togo[togo[go]] == -1 or go == -1:
                    s_8 += 1
                    break
                donut += 1
                break
            elif togo[go] > 0:
                go = togo[go]
            else:
                break

    return [sorce, donut, stick, s_8]


print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))
