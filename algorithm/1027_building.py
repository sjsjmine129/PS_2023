
n = int(input())
temp = input().split()
list = [int(item) for item in temp]

score = [0 for _ in range(n)]

for i in range(0, n-1):
    m = -1000000000
    for j in range(i+1, n):
        inclination = (list[j]-list[i])/(j-i)

        if m < inclination:  # 최대값 바꾸기
            m = inclination
            score[i] += 1
            score[j] += 1


print(max(score))
