from sys import stdin, stdout
from math import comb

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
    n, k = IMI()
    if k >= 30:
        final.append(str(n + 1))
    else:
        final.append(str(min(n + 1, 1 << k)))
        

stdout.write("\n".join(final))