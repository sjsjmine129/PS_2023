from itertools import combinations

n = int(input())
# Define the range of numbers (0 to 9)
numbers = list(range(10))

all = []
for i in range(1, 11):
    combinations_list = list(combinations(numbers, i))
    for j in combinations_list:
        sorted_str = ''.join(sorted(map(str, j), reverse=True))
        result = int(sorted_str)
        all.append(result)

all.sort()
# print(all)
if n >= len(all):
    print(-1)
else:
    print(all[n])
