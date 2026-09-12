from sys import stdin, stdout
from collections import Counter
from math import inf

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
    b = ILI()
    
    nr = True
    cnr = 0
    for i in range(n):
        if a[i] < b[i]:
            nr = False
        cnr += (a[i] - b[i])
    
    sa = sorted(a)
    sb = sorted(b)
    
    r = True
    cr = m
    for i in range(n):
        if sa[i] < sb[i]:
            r = False
        cr += (sa[i] - sb[i])
        
    ans = -1
    if nr and r:
        ans = min(cnr, cr)
    elif nr:
        ans = cnr
    elif r:
        ans = cr
    
    final.append(str(ans))

stdout.write("\n".join(final))
