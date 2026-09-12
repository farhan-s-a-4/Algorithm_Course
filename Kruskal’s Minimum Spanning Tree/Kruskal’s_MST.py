import sys

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    dsu = DSU(n)
    mst = []
    total_cost = 0

    for u, v, w in edges:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append((u, v, w))
            total_cost += w

    return total_cost, mst

if __name__ == "__main__":
    data = sys.stdin.read().split()
    n = int(data[0])
    edges = [list(map(int, data[i:i+3])) for i in range(1, len(data), 3)]
    cost, mst = kruskal(n, edges)
    print(cost)
    for u, v, w in mst:
        print(u, v, w)