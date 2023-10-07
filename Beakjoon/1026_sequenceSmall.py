length = int(input())

temp = input().split()
a = [int(x) for x in temp]

temp2 = input().split()
b = [int(x) for x in temp2]

a.sort()
b.sort(reverse=True)


S = 0
for i in range(length):
    S += a[i]*b[i]

print(S)
