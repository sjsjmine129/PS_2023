n = int(input())

store = {}

for i in range(n):
    temp = input()
    num = len(temp)
    for j in temp:
        num -= 1
        if j not in store:
            store[j] = 10**num
        else:
            temp = store[j] + 10**num
            store[j] = temp

value = []
for i in store:
    value.append(store[i])

value.sort(reverse=True)

num = [i for i in range(10)]

ret = 0
for i in value:
    m = num.pop()
    ret += m*i

print(ret)
