N, M = map(int, input().split())

human = [0 for i in range(N+1)]
human[0] = -1

a = [int(x) for x in input().split()]

party = []

for i in range(M):
    party.append([int(x) for x in input().split()])

q = []

for i in range(1, len(a)):
    human[a[i]] = 1
    q.append(a[i])

# print(human)
# print(q)
# for i in range(M):
#     print(party[i])

while len(q) > 0:
    temp = q.pop()

    for i in range(M):

        # 이미 말 못하는 곳
        if party[i][0] == -1:
            continue

        # 가능성이 있는 곳
        for j in range(1, len(party[i])):
            # 그 줄에 진실 아는 자 존재시
            if party[i][j] == temp:
                party[i][0] = -1
                for k in range(1, len(party[i])):
                    if human[party[i][k]] == 0:
                        human[party[i][k]] = 1
                        q.append(party[i][k])
                break

# print(human)
# for i in range(M):
#     print(party[i])

num = 0

for i in range(M):
    if party[i][0] != -1:
        num += 1

print(num)
