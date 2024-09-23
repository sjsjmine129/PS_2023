[n, m] = map(int, input().split())

boxes = []
checker = []

for i in range(n):
    temp = input().split()
    box = []
    for i in range(m):
        if temp[i] != "0":
            box.append(i)

    if len(box) == 1 and box[0] not in checker:
        checker.append(box[0])
    elif len(box) != 0:
        boxes.append(box)

# for i in boxes:
#     print(i)

print(max(0, len(boxes)-1))
