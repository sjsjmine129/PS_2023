def solution(r1, r2):

    R1 = r1**2
    R2 = r2**2

    answer = r2 - r1 + 1
    # print(answer)

    for i in range(1, r2+1):
        I = i**2

        h = int((R2-I)**0.5)

        if I >= R1:
            answer += h
        else:
            l = int((R1-I)**0.5)
            # print("l :", l)
            if l**2 + I == R1:
                answer += 1

            # print("h :", h, "l :", l)
            answer += h - l

        # print(answer)

    answer = answer * 4

    return answer


print(solution(2, 3))
