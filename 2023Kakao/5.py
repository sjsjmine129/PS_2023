def solution(n, tops):

    green = 1
    purple = 0

    for i in range(n):
        b_green = green
        b_purple = purple

        if tops[i] == 1:  # A
            green = b_green*3+b_purple*2
            purple = b_green+b_purple
        else:  # B
            green = b_green*2+b_purple
            purple = b_green+b_purple

    ret = green+purple
    return ret % 10007


print(solution(2, [0, 1]))
