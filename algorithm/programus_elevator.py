def solution(storey):
    s = str(storey)
    l = []
    for i in s:
        l.append(int(i))

    l.reverse()

    answer = 0

    for i in range(len(l)):
        num = l[i]

        if num <= 4:
            answer += num

        elif num == 10:
            if i == len(l)-1:
                answer += 1
            else:
                l[i+1] += 1

        elif num >= 6:
            answer += 10-num
            if i == len(l)-1:
                answer += 1
            else:
                l[i+1] += 1

        else:
            if i == len(l)-1:
                answer += 5
            else:
                if l[i+1] <= 4:
                    answer += 5
                elif l[i+1] >= 5:
                    answer += 5
                    l[i+1] += 1

    return answer


print(solution(55))
