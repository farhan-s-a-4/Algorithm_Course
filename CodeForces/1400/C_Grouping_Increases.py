from sys import stdin, stdout
from math import inf
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().split()))
final = []
for _ in range(II()):
    n = II()
    a = ILI()
    u, v = inf, inf
    ans0 = 0
    for i in a:
        if u >= i:
            u = i
        elif v >= i:
            v = i
        else:
            u = i
            ans0 += 1
        if u > v:
            u, v = v, u
    final.append(ans0)
stdout.write("\n".join(map(str, final)))