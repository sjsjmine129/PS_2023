def solution(book_time):
    answer = 0

    time = []
    for i in book_time:
        [a, b] = i[0].split(':')
        s = int(a)*60 + int(b)
        time.append([s, 1])
        [c, d] = i[1].split(':')
        e = int(c)*60 + int(d) + 10
        time.append([e, -1])

    time.sort(key=lambda x: (x[0], x[1]))
    stack = []

    for i in time:
        if (not stack):
            stack.append(i)
        elif i[1] == 1:
            stack.append(i)
        else:
            stack.pop()

        if len(stack) > answer:
            answer = len(stack)

    return answer


print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
