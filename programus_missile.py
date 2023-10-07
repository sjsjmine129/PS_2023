def solution(targets):
    targets.sort(key=lambda x: x[1])

    temp = 0
    answer = 0

    for target in targets:
        if temp <= target[0]:
            temp = target[1]
            answer += 1

    return answer


solution([[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]])
