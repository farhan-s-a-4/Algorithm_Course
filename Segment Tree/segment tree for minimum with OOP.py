from math import ceil, log2

class SegmentTree:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.size = self._calculate_size()
        self.tree = [None] * self.size
        self._build(0, self.n - 1, 0)

    def _calculate_size(self):
        if self.n == 0:
            return 0
        size = 1
        for _ in range(ceil(log2(self.n))):
            size <<= 1
            size += 1
        return size

    def _build(self, start, end, node):
        if start == end:
            self.tree[node] = self.data[start]
            return
        
        mid = (start + end) // 2

        self._build(start, mid, node * 2 + 1)
        self._build(mid + 1, end, node * 2 + 2)

        self.tree[node] = min(self.tree[node * 2 + 1], self.tree[node * 2 + 2])


if __name__ == "__main__":
    a = list(map(int, input("Enter space-separated integers: ").split()))
    
    seg_tree = SegmentTree(a)
    
    print(seg_tree.size)
    print(seg_tree.tree[0])
