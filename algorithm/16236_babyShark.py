N = int(input())

list = []

for i in range(N):
    list.append([int(x) for x in input().split()])


for i in range(N):
    for j in range(N):
        if list[i][j] == 9:
            list[i][j] = 0
            x = j
            y = i

# print(x, y)


dir = [[0, -1], [-1, 0], [1, 0], [0, 1]]

next = [[x, y, 0]]  # 3번째는 거리
size = 2
eat = 0

store = []
store_level = 0

time_sum = 0


# 지나온곳 표시한거 없애는 함수
def reset():
    for i in range(N):
        for j in range(N):
            if list[i][j] == 10:
                list[i][j] = 0
            elif list[i][j] >= 100:
                list[i][j] = list[i][j]//100
            elif list[i][j] == -1:
                list[i][j] = 0


while len(next) > 0:

    now = next.pop(0)

    if list[now[1]][now[0]] == 0:
        list[now[1]][now[0]] = 10  # 이동체크
    elif list[now[1]][now[0]] < 10:
        list[now[1]][now[0]] = list[now[1]][now[0]]*100

    for go in dir:

        tempx = now[0]+go[0]
        tempy = now[1]+go[1]
        if tempx >= 0 and tempx < N and tempy >= 0 and tempy < N:  # 범위 안넘음 = 이동시도

            if list[tempy][tempx] < size and list[tempy][tempx] > 0:  # 먹을 수 있는 놈
                store.append([tempx, tempy])
                list[tempy][tempx] = list[tempy][tempx]*100

            elif list[tempy][tempx] == size or list[tempy][tempx] == 0:  # 이동은 가능한 경우
                if list[tempy][tempx] == 0:
                    list[tempy][tempx] = list[tempy][tempx]*100  # 이동체크
                else:
                    list[tempy][tempx] = list[tempy][tempx]*100
                next.append([tempx, tempy, now[2]+1])  # 다음 체크할 친구 추가

    #
    if len(next) == 0 or next[0][2] != now[2]:
        if len(store) > 0:  # 먹을 수 있는놈 있을 때
            that = store[0]
            for k in store:
                if k[1] < that[1]:
                    that = k
                elif k[1] == that[1] and k[0] < that[0]:
                    that = k

            eat += 1
            if eat == size:
                eat = 0
                size += 1
                if size > 9:
                    size = 9

            list[that[1]][that[0]] = -1  # 그자리 없앰

            # 여기로 이동하고 다시 시작
            next = []  # 기존 삭제
            next.append([that[0], that[1], 0])  # 새 시작점
            store = []
            time_sum += (now[2]+1)  # 시간 추가

            # for i in list:
            #     print(i)
            # print("now ", now)
            # print("next ", that[0], that[1])
            # print("size ", size)
            # print("eat ", eat)
            # print("time", time_sum)
            # print("===========")
            reset()  # 지나온곳 체크 없앰
            # for i in list:
            #     print(i)
            # print(next)
            # print("############")

# for i in list:
#     print(i)

print(time_sum)
