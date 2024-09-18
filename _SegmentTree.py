from math import ceil, log2

A = [1, 2, 3, 4, 5]

height = ceil(log2(len(A)))
tree_size = 1 << (height+1)
tree = [0] * tree_size

# #or
# tree_size = 4 * len(A)
# tree = [0] * tree_size


def build(node, start, end):
    # 리프 노드
    if start == end:
        tree[node] = A[start]
        return

    # 중간 노드
    mid = (start + end) // 2  # 반으로 쪼갬

    # 왼쪽 자식
    build(node*2, start, mid)
    # 오른쪽 자식
    build(node*2+1, mid+1, end)

    # 두 자식의 값 합치기
    tree[node] = tree[node*2] + tree[node*2+1]
    return


build(1, 0, len(A)-1)
print(tree)


def getSum(node, start, end, findStart, findEnd):
    #                순회용
    if end < findStart or start > findEnd:  # 순회중 범위가 밖인 경우
        return 0
    elif start >= findStart and end <= findEnd:  # 순회중 범위에 포함인 경우
        return tree[node]
    else:  # 일부만 범위인 경우
        mid = (start+end)//2
        return getSum(node*2, start, mid, findStart, findEnd) + getSum(node*2+1, mid+1, end, findStart, findEnd)


print(getSum(1, 0, len(A)-1, 1, 3))


def upDate(node, start, end, index, newValue):
    # 범위 밖
    if start > index or end < index:
        return

    # 범위안 -> 갱신 필요
    # 리프 노드
    if start == end:
        tree[node] = newValue
        return

    # 중간 노드
    mid = (start + end) // 2  # 반으로 쪼갬

    # 왼쪽 자식
    upDate(node*2, start, mid, index, newValue)
    # 오른쪽 자식
    upDate(node*2+1, mid+1, end, index, newValue)

    # 두 자식의 값 합치기
    tree[node] = tree[node*2] + tree[node*2+1]
    return


A[2] = 5
upDate(1, 0, len(A)-1, 2, 5)
print(tree)
