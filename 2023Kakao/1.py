def solution(friends, gifts):

    n = len(friends)
    score = {}
    history = {}
    result = {}

    for i in friends:
        score[i] = 0
        result[i] = 0

    for i in gifts:
        temp = i.split(" ")

        if i in history:
            history[i] = history[i]+1
            history[temp[1]+" "+temp[0]] = history[temp[1]+" "+temp[0]]-1
        else:
            history[i] = 1
            history[temp[1]+" "+temp[0]] = -1

        score[temp[0]] += 1
        score[temp[1]] -= 1

    max = 0
    for i in range(n):
        for j in range(i+1, n):
            key = friends[i]+" "+friends[j]
            if key in history and history[key] > 0:
                result[friends[i]] += 1
            elif key in history and history[key] < 0:
                result[friends[j]] += 1
            elif score[friends[i]] > score[friends[j]]:
                result[friends[i]] += 1
            elif score[friends[i]] < score[friends[j]]:
                result[friends[j]] += 1

        if max < result[friends[i]]:
            max = result[friends[i]]

    print(history)
    print(score)
    print(result)
    return max
