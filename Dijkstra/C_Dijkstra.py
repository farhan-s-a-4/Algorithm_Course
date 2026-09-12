from sys import stdin, stdout
import heapq

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

def dijkstra(graph, n):
    distances = [float('inf')] * (n + 1)
    distances[1] = 0
    parents = [0] * (n + 1)
    
    pq = [(0, 1)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > distances[u]:
            continue
            
        for v, weight in adj[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                parents[v] = u
                heapq.heappush(pq, (distances[v], v))
                
    if distances[n] == float('inf'):
        return None
    else:
        path = []
        curr = n
        while curr != 0:
            path.append(curr)
            curr = parents[curr]
        return path[::-1]

if __name__ == "__main__":
    n, m = IMI()
    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        adj[v].append((u, w))

    path = dijkstra(adj, n)
    
    if path:
        stdout.write(" ".join(map(str, path)))
    else:
        stdout.write('-1')