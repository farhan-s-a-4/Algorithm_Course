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

final = []
for _ in range(II()):
    n = II()
    a = [0] + ILI()
    P = [0] * (n + 2)
    for i in range(1, n + 1):
        P[i] = P[i - 1] + abs(a[i])
        
    S = [0] * (n + 2)
    for i in range(n, 0, -1):
        S[i] = S[i + 1] + a[i]
    max_sum = S[1]
    best_M = -1
    for i in range(1, n + 1):
        if a[i] > 0:
            current_sum = P[i - 1] - a[i] + S[i + 1]
            if current_sum > max_sum:
                max_sum = current_sum
                best_M = i
                
    s = [1] * (n + 2)
    if best_M != -1:
        for i in range(1, best_M):
            s[i] = 1 if a[i] > 0 else -1
        s[best_M] = -1
        for i in range(best_M + 1, n + 1):
            s[i] = 1
    E = []
    for i in range(1, n + 1):
        if s[i] * s[i + 1] == -1:
            E.append(i)
    ans = deque()
    for x in reversed(E):
        if a[x] > 0:
            ans.appendleft(x)
        else:
            front_val = ans.popleft()
            ans.appendleft(x)
            ans.appendleft(front_val)
            
    final.append(str(len(ans)))
    final.append(" ".join(map(str, ans)))

stdout.write("\n".join(final) + "\n")