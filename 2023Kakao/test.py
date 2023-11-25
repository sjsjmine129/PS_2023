get = [1, 2, 3, 4, 5]

for i in range(len(get)):
    temp = get.pop(i)
    get.insert(i, temp)

print(get)
