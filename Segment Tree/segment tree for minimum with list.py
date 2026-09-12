from math import ceil, log2

def create_tree(a, tree, start, end, node):
    if start == end:
        tree[node] = a[start]
        return
    
    mid = (start + end) // 2

    create_tree(a, tree, start, mid, node * 2 + 1)
    create_tree(a, tree, mid + 1, end, node * 2 + 2)

    tree[node] = min(tree[node * 2 + 1], tree[node * 2 + 2])
    return

if __name__ == "__main__":
    a = list(map(int, input().split()))
    n = len(a)
    size = 1
    for _ in range(ceil(log2(n))):
        size <<= 1
        size += 1
    print(size)
    tree = [None] * size
    create_tree(a, tree, 0, n - 1, 0)
    print(tree)