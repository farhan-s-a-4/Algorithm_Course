from sys import stdin, stdout
from math import log, floor

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
    if k == 1:
        final.append(str(n))
        continue
    count = 0
    while n > 0:
        count += n % k
        n = n // k
    final.append(str(count))

stdout.write("\n".join(final))