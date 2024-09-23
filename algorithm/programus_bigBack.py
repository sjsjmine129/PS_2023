def solution(numbers):
    num = [[value, index] for index, value in enumerate(numbers)]
    answer = [-1]*len(numbers)

    stack = [num[0]]
    del num[0]

    for i in num:
        while len(stack) > 0:
            if stack[-1][0] < i[0]:
                temp = stack.pop()
                answer[temp[1]] = i[0]
            else:
                break

        stack.append(i)

    return answer


print(solution([9, 1, 5, 3, 6, 2]))
