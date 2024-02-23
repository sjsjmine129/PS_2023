from itertools import combinations

[n, k] = map(int, input().split())

word = []
wordNum = 0

have = ["a", "n", "t", "i", "c"]
alphabet = set()

for i in range(n):
    temp = input()
    w = temp[4:-4]
    new = set()
    for j in w:
        if j not in have:
            new.add(j)
            alphabet.add(j)

    if len(new) == 0:
        wordNum += 1
    else:
        if len(new) <= k-5:
            word.append(new)
# print(word)

if k < 5:
    print(0)
    exit()
elif k == 5:
    print(wordNum)
    exit()
elif k-5 >= len(alphabet):
    print(n)
    exit()

# learn a, n, t, i, c
k -= 5

combinations_list = list(combinations(alphabet, k))


ret = 0
for i in combinations_list:
    temp = 0
    temp_set = set(i)
    for j in word:
        if temp_set >= j:
            temp += 1
    if temp > ret:
        ret = temp

print(wordNum+ret)
