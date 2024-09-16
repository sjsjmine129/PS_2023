
def BinarySearch(n, findList, start, end):
    if start > end:
        print("no item")
        return

    index = (start + end) // 2

    if n == findList[index]:
        print(index)
    elif n < findList[index]:
        BinarySearch(n, findList, start, index-1)
    else:
        BinarySearch(n, findList, index+1, end)


##########################################################
inputList = [int(x) for x in input().split()]
inputList.sort()
# print(inputList)

findNum = int(input())

BinarySearch(findNum, inputList, 0, len(inputList)-1)
