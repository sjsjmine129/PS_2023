def solution(r1, r2):
    R1 = r1**2
    R2 = r2**2

    answer = 0
    for i in range(1, r2+1):
        for j in range(1, r2+1):
            len = i**2 + j**2
            if len > R2:
                break
            elif len >= R1 and len <= R2:
                answer += 1

    answer = answer * 4 + 4*(r2-r1+1)
    return answer


print(solution(2, 3))
