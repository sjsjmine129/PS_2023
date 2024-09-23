n, m = map(int, input().split())
board = []
for i in range(n):
    temp = [int(i) for i in input().split()]
    board.append(temp)

two_two = [[0, 0], [0, 1], [1, 0], [1, 1]]
one_four = [[0, 0], [0, 2], [0, 3], [0, 1]]
two_three = [[[0, 0], [0, 1], [0, 2], [1, 2]], [[0, 0], [1, 0], [1, 1], [1, 2]], [[0, 2], [1, 0], [1, 1], [1, 2]], [[0, 0], [
    0, 1], [0, 2], [1, 0]], [[0, 0], [0, 1], [1, 1], [1, 2]], [[0, 1], [0, 2], [1, 0], [1, 1]], [[0, 1], [1, 0], [1, 1], [1, 2]], [[0, 0], [0, 1], [0, 2], [1, 1]]]

ret = 0
for i in range(n):
    for j in range(m):
        # 2*2
        if i <= n-2 and j <= m-2:
            temp = 0
            for k in two_two:
                temp += board[i+k[0]][j+k[1]]
            # print(temp)
            if temp > ret:
                ret = temp

        # 1*4
        if j <= m-4:
            temp = 0
            for k in one_four:
                temp += board[i+k[0]][j+k[1]]
            # print(temp)
            if temp > ret:
                ret = temp

        # 4*1
        if i <= n-4:
            temp = 0
            for k in one_four:
                temp += board[i+k[1]][j+k[0]]
            # print(temp)
            if temp > ret:
                ret = temp

        # 3*2
        if i <= n-3 and j <= m-2:
            for shape in two_three:
                temp = 0
                for k in shape:
                    temp += board[i+k[1]][j+k[0]]
                # print(temp)
                if temp > ret:
                    ret = temp

        # 2*3
        if i <= n-2 and j <= m-3:
            for shape in two_three:
                temp = 0
                for k in shape:
                    temp += board[i+k[0]][j+k[1]]
                # print(temp)
                if temp > ret:
                    ret = temp
print(ret)
