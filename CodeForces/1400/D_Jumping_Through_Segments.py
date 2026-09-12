from sys import stdin, stdout
from math import inf
def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))
final = []
def check(k):
    low, high = 0, 0
    for l, r in intervals:
        reach_low = low - k
        reach_high = high + k
        
        low = max(reach_low, l)
        high = min(reach_high, r)

        if low > high:
            return False

    return True

for _ in range(II()):
    n = II()
    intervals = []
    for _ in range(n):
        l, r = IMI()
        intervals.append((l, r))

    L, R =0, 10**9

    while L<=R:
        m = (L+R)//2

        if check(m):
            R = m-1
        else:
            L = m+1

    final.append(str(L))

stdout.write("\n".join(final))