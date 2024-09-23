
n = int(input())
temp = input().split()
p = [int(item) for item in temp]
temp2 = input().split()
s = [int(item) for item in temp2]


card = [i for i in range(n)]
next = [0 for i in range(n)]

time = 0
while True:
    # 끝인지 확인
    checker = 0
    for i in range(0, len(p)):
        if i % 3 != p[card[i]]:
            checker = 1
            break
    if checker == 0:
        print(time)
        break

    # 1번 섞기
    for i in range(0, n):
        next[s[i]] = card[i]

    # 처음과 같은지 확인하면서 정리
    checker = 0
    for i in range(0, n):
        card[i] = next[i]
        if next[i] != i:
            checker = 1

    if checker == 0:
        print(-1)
        break

    # print(card)
    time += 1
