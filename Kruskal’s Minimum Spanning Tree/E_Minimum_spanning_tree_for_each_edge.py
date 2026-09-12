from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))
def SI():
    return stdin.readline().strip()
def SLI():
    return stdin.readline().split()

class DSU:
    def __init__(self, n, must):
        self.parent = list(range(n + 1))
        self.cost = 0
        self.rank = [0] * (n+1)
        self.union(must[0], must[1], must[2])

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y, w):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.cost+=w
            if self.rank[py] > self.rank[px]:
                px, py = py, px
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1

def modified_kruskal(n, must, edges):
    dsu = DSU(n, must)
    for u, v, w in edges:
        if [u,v,w] == must:
            continue
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v, w)
    return str(dsu.cost)

final = []
n, m = IMI()
edges = [ILI() for __ in range(m)]
se = sorted(edges, key=lambda x: x[2])
for _ in range(m):
    final.append(modified_kruskal(n, edges[_], se))

stdout.write("\n".join(map(str, final)))