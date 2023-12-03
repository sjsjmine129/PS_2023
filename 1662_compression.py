str = input()

stack = []

final = ''

length = 0

for i in str:
    if i != ')':  # 나머지 경우
        stack.append(i)

    else:  # )인경우
        now = 0
        while True:
            temp = stack.pop()
            if temp == '(':
                multi = int(stack.pop())
                len_sum = multi*now*(-1)
                if len_sum != 0:
                    stack.append(len_sum)
                break
            else:
                int_temp = int(temp)
                if int_temp < 0:
                    now += int_temp*(-1)
                else:
                    now += 1

ret = 0
for i in stack:
    int_i = int(i)
    if int_i < 0:
        ret += int_i*(-1)
    else:
        ret += 1

# print(stack)
print(ret)
