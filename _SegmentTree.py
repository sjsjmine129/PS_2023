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
