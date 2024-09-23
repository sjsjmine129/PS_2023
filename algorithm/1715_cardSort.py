from queue import PriorityQueue

n = int(input())
cards = PriorityQueue()
for i in range(n):
    temp = int(input())
    cards.put(temp)

# print(cards.qsize())
num = 0

for i in range(n-1):
    a = cards.get()
    b = cards.get()

    dnum = a+b
    num += dnum

    cards.put(dnum)


print(num)
