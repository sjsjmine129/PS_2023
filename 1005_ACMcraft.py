t = int(input())

for mianLoop in range(t):
    [n, k] = map(int, input().split())
    time = [int(i) for i in input().split()]
    time.insert(0, -1)

    record = [-1 for _ in range(n+1)]

    dependency = [[] for _ in range(n+1)]

    for i in range(k):
        [x, y] = map(int, input().split())
        dependency[y].append(x)

    def findTime(node):
        # 필요한게 없는 경우 -> 그 시간
        if len(dependency[node]) == 0:
            record[node] = time[node]
            return time[node]
        # 필요한계 있는 경우 -> 전놈 중 최대값 + 그시간
        else:
            temp = []
            for j in dependency[node]:
                if record[j] != -1:
                    temp.append(record[j])
                else:
                    cal = findTime(j)
                    record[j] = cal
                    temp.append(cal)
            return max(temp)+time[node]

    w = int(input())
    print(findTime(w))
