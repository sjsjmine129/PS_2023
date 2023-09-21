import math

# 명수 입력 받기
n = int(input())

# 친구 관계 입력 받기 as edge
E = []
for i in range(0, n):
    line = input()
    for j in range(0, len(line)):
        if (line[j] == 'Y'):
            E.append([i, j])

# print(E)


max = 0

# find out each person's friends and friends of friends
for i in range(0, n):
    count = 0
    friends_1 = [i]
    friends_2 = []

    # direct friends
    for e in E:
        if (i == e[0]):
            friends_1.append(e[1])

    # indirect friends
    for f in friends_1:
        for e in E:
            if (f == e[0] and e[1] not in friends_1 and e[1] not in friends_2):
                friends_2.append(e[1])

    # compare
    count = len(friends_1) + len(friends_2)
    if (count > max):
        max = count


print(max-1)
