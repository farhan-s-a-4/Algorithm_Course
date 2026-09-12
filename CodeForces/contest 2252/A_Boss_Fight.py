from sys import stdin, stdout
from collections import Counter

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
    
    s = sum(a)
    
    counts = Counter(a)
    x, mcount = counts.most_common(1)[0]
    
    others = n - mcount
    allowed = others + 2
    if mcount > allowed:
        s -= (mcount - allowed) * x
        
    final.append(str(s))

stdout.write("\n".join(final))