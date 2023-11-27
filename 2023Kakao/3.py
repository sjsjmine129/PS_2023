# not solved -> 2개, 4개인 경우만 품
def solution(dice):
    n = len(dice)
    if n == 2:
        a = sum(dice[0])
        b = sum(dice[1])
        if a > b:
            return [1]
        elif a < b:
            return [2]

    if n == 4:
        a_1 = [dice[0], dice[1]]
        a_2 = [dice[2], dice[3]]

        b_1 = [dice[0], dice[2]]
        b_2 = [dice[1], dice[3]]

        c_1 = [dice[0], dice[3]]
        c_2 = [dice[1], dice[2]]

        a_1_can = []
        a_2_can = []
        b_1_can = []
        b_2_can = []
        c_1_can = []
        c_2_can = []

        for i in range(6):
            for j in range(6):
                a_1_can.append(a_1[0][i]+a_1[1][j])
                a_2_can.append(a_2[0][i]+a_2[1][j])
                b_1_can.append(b_1[0][i]+b_1[1][j])
                b_2_can.append(b_2[0][i]+b_2[1][j])
                c_1_can.append(c_1[0][i]+c_1[1][j])
                c_2_can.append(c_2[0][i]+c_2[1][j])

        a_1_win = 0
        a_2_win = 0
        b_1_win = 0
        b_2_win = 0
        c_1_win = 0
        c_2_win = 0

        for i in range(36):
            for j in range(36):
                if a_1_can[i] > a_2_can[j]:
                    a_1_win += 1
                if a_1_can[i] < a_2_can[j]:
                    a_2_win += 1
                if b_1_can[i] > b_2_can[j]:
                    b_1_win += 1
                if b_1_can[i] < b_2_can[j]:
                    b_2_win += 1
                if c_1_can[i] > c_2_can[j]:
                    c_1_win += 1
                if c_1_can[i] < c_2_can[j]:
                    c_2_win += 1

        m = max(a_1_win, a_2_win, b_1_win, b_2_win, c_1_win, c_2_win)

        if m == a_1_win:
            return [1, 2]
        elif m == a_2_win:
            return [3, 4]
        elif m == b_1_win:
            return [1, 3]
        elif m == b_2_win:
            return [2, 4]
        elif m == c_1_win:
            return [1, 4]
        elif m == c_2_win:
            return [2, 3]
