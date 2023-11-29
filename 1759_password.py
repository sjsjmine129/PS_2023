L, C = map(int, input().split())
a = input().split()
a = sorted(a)

v_max = L-2
c_max = L-1

# print(a, v_max, c_max)


def find_all(str, index, v, c):
    if len(str) == L:
        print(str)
    elif index < C:
        next = a[index]
        if (next == 'a' or next == 'e' or next == 'i' or next == 'o' or next == 'u') and v < v_max:
            # 모음인 경우

            find_all(str+next, index+1, v+1, c)  # 넣는 경우
            find_all(str, index+1, v, c)  # 안 넣는 경우
        elif (next == 'a' or next == 'e' or next == 'i' or next == 'o' or next == 'u'):
            find_all(str, index+1, v, c)  # 안 넣는 경우
        elif c < c_max:
            # 자음인 경우
            find_all(str+next, index+1, v, c+1)  # 넣는 경우
            find_all(str, index+1, v, c)  # 안넣는 경우
        else:
            find_all(str, index+1, v, c)  # 안넣는 경우


find_all('', 0, 0, 0)
