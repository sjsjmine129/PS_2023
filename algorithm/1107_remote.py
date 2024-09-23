goal = int(input())
n = int(input())
if n != 0:
    wrong = input().split()
else:
    wrong = []
# print(wrong)

if goal == 100:
    print(0)
    exit()
elif goal == 101 or goal == 99:
    print(1)
    exit()
elif goal == 102 or goal == 98:
    print(2)
    exit()


num = 0
big = goal-1
small = goal+1

just = goal-100
if just < 0:
    just = (-1)*just


while True:
    small = small - 1
    big = big+1

    if small == 100:
        print(num)
        break
    elif big == 100:
        print(num)
        break

    if small >= 0:
        checker = True
        str_small = str(small)
        for i in range(len(str_small)):
            if str_small[i] in wrong:
                checker = False
                break
        if checker == True:
            # print(small)
            if num+len(str_small) >= just:
                print(just)
            else:
                print(num+len(str_small))
            break

    checker = True
    str_big = str(big)
    for i in range(len(str_big)):
        if str_big[i] in wrong:
            checker = False
            break
    if checker == True:
        # print(big)
        if num+len(str_big) >= just:
            print(just)
        else:
            print(num+len(str_big))
        break

    num += 1
