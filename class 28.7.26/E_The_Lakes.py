from sys import stdin, stdout
from collections import deque

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


def bfs(start_x, start_y, n, m, a):
    s = a[start_x][start_y]
    a[start_x][start_y] = 0
    q = deque([(start_x, start_y)])
    
    while q:
        x, y = q.popleft()
        for nx, ny in [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]:
            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] > 0:
                s += a[nx][ny]
                a[nx][ny] = 0
                q.append((nx, ny))
    return s

final = []
for _ in range(II()):
    n, m = IMI()
    a = [ILI() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] > 0:
                ans = max(ans, bfs(i, j, n, m, a))
    final.append(str(ans))

stdout.write("\n".join(final) + "\n")