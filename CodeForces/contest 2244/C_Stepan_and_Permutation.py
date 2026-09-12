from sys import stdin, stdout
from math import gcd

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
    n, x, y = IMI()
    a = ILI()
    z = gcd(x, y)

    if z == 1:
        final.append("YES")
        continue

    for i in range(n):
        temp = (abs(a[i] - i - 1)) % z
        if temp != 0:
            final.append("NO")
            break
    else:
        final.append("YES")
    

stdout.write("\n".join(final))