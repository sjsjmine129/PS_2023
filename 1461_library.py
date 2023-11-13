N, M = map(int, input().split())

list = [int(i) for i in input().split()]

minus = []
plus = []

for i in list:
    if i < 0:
        minus.append(-1*i)
    else:
        plus.append(i)

minus.sort(reverse=True)
plus.sort(reverse=True)

# print(minus)
# print(plus)

step = 0

i = 0
max = 0

while i < len(minus):
    step += 2*minus[i]
    if i == 0:
        max = minus[i]
    i += M

i = 0
while i < len(plus):
    step += 2*plus[i]
    if i == 0 and max < plus[i]:
        max = plus[i]
    i += M

print(step-max)
