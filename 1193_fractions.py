import math

x = int(input())
j = 0
i = 1

for i in range(1, x+1):
    j += i
    if j >= x:
        break

row = i+1

gap = j-x+1
other = row-gap

if (i % 2 == 0):
    print(str(other)+'/'+str(gap))
else:
    print(str(gap)+'/'+str(other))
