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
    n, m = IMI()
    a = ILI()
    q = deque((i, x) for i, x in enumerate(a))
    time = 0
    #print(a, q)
    while q:
        a_max = max(el[1] for el in q)
        i, v = q.popleft()
        #print(time)
        if v == a_max:
            time += 1
            if i == m:
                break
        else:
            q.append((i,v))
    final.append(f"{time}")
        
stdout.write("\n".join(final))
