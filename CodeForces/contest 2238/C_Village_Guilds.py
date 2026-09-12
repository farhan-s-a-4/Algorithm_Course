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

final = []
for _ in range(II()):
    n = II()
    p = [0, 0] + ILI() 
    
    depth = [0] * (n + 1)
    for i in range(2, n + 1):
        depth[i] = depth[p[i]] + 1
        
    m1 = depth[:]
    m2 = depth[:]
    
    for i in range(n, 1, -1):
        pi = p[i]
        child_max = m1[i]
        
        if child_max > m1[pi]:
            m2[pi] = m1[pi]
            m1[pi] = child_max
        elif child_max > m2[pi]:
            m2[pi] = child_max
            
    ans = 0
    for i in range(1, n + 1):
        ans += m2[i] - depth[i] + 1
        
    final.append(str(ans))

stdout.write("\n".join(final))