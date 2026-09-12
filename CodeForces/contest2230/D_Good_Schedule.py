from sys import stdin, stdout
import sys

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

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    b = ILI()
    max_start = [0] * (n + 2)
    
    first_blocker = [n + 1] * (n + 2)
    
    parent = list(range(n + 3))
    
    def find(i):
        path = []
        while parent[i] != i:
            path.append(i)
            i = parent[i]
        for node in path:
            parent[node] = i
        return i
    
    for i in range(1, n + 1):
        u = a[i-1]
        v = b[i-1]
        
        if u != v:
            for val in (u, v):
                if val == 1:
                    r_limit = i
                else:
                    r_limit = max_start[val - 1]
                    
                l_limit = max_start[val]
                
                if r_limit > l_limit:
                    curr = find(l_limit + 1)
                    while curr <= r_limit:
                        first_blocker[curr] = i
                        parent[curr] = find(curr + 1)
                        curr = find(curr)
        else:
            if u == 1:
                max_start[1] = i
            else:
                if max_start[u - 1] > max_start[u]:
                    max_start[u] = max_start[u - 1]
                    
    ans = 0
    for i in range(1, n + 1):
        ans += first_blocker[i] - i
    final.append(str(ans))

stdout.write("\n".join(final))
