n = int(input())
list = []
for i in range(n):
    list.append(input())


for str in list:
    i = 0
    length = len(str)
    if str[length-1] == '0':
        print("NO")
        continue

    while i < length:
        if str[i] == '0':
            if i+1 >= length or str[i+1] == '0':
                print("NO")
                break
            else:
                i += 2
        else:
            i += 1
            if i >= length or str[i] == '1':
                print("NO")
                break
            i += 1
            if i >= length or str[i] == '1':
                print("NO")
                break

            while i < length and str[i] == '0':
                i += 1

            if i >= length:
                print("NO")
                break

            check = 0
            while i < length and str[i] == '1':
                check += 1
                i += 1

            if check >= 2 and i+1 < length and str[i] == '0' and str[i+1] == '0':
                i -= 1

        # print(i)
        if i == length:
            print('YES')
