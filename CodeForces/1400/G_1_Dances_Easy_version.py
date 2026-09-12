from sys import stdin, stdout
from math import inf

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))

final = []
for _ in range(II()):
    n, m = IMI()
    a = [1] + sorted(ILI())
    b = sorted(ILI())
    
    i = 0
    for j in range(n):
        if a[i] < b[j]:
            i += 1
            
    final.append(str(n - i))

stdout.write("\n".join(final))
