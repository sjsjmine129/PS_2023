n = int(input())
tower = [int(x) for x in input().split()]
result = [0 for x in range(n)]
s = []

for i in range(n):
    if len(s) == 0:
        s.append(i)
    else:
        temp = s.pop(-1)
        while tower[temp] < tower[i] and len(s) != 0:
            temp = s.pop(-1)

        if tower[temp] > tower[i]:  # 더 긴놈 만남
            result[i] = temp+1
            s.append(temp)
        s.append(i)


for i in result:
    print(i, end=' ')
print()
