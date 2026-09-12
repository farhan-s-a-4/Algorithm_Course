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


def dijkstra(adj, start, end, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    
    pq = [(0, start)]
    
    while pq:
        d, u = heapq.heappop(pq)
        
        if d > distances[u]:
            continue
            
        for n, w in adj[u]:
            if distances[u] + w < distances[n]:
                distances[n] = distances[u] + w
                heapq.heappush(pq, (distances[n], n))
                
    if distances[end] == float('inf'):
        return "NO"
    else:
        return str(distances[end])

final = []

for _ in range(II()):
    n, m = IMI()    
    adj = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v, w = IMI()
        adj[u].append((v, w))

    start, end = IMI()

    final.append(dijkstra(adj, start, end, n))

stdout.write("\n".join(final) + "\n")

