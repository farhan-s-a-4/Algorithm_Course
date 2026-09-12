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
    n,k = IMI()
    a = ILI()
    if k >= 3 :
        final.append(str(0))
        continue
    a.sort()
    ans = a[0]
    for i in range(1,n):
        ans = min(ans,a[i]-a[i-1])
    if k == 1 :
        final.append(str(ans))
        continue
    for j in range(n):
        i, k = 0,n-1 
        while i < j and i <= k :
            s = a[i]+a[k] 
            d = a[j] - s
            ans = min(ans,abs(d))
            if d > 0 :
                i += 1
            else :
                k-= 1
    final.append(str(ans))
stdout.write("\n".join(final))