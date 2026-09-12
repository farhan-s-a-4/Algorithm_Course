from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI(m):
    return list(map(lambda x: int(x)-m, stdin.readline().split()))
def SI():
    return stdin.readline().strip()
def SLI():
    return stdin.readline().split()

final = []
for _ in range(II()):
    n, m = IMI()
    a = sorted(ILI(m))
    ans = 0
    for i in range(n):
        l,r=i,n-1-i
        if r<l:
            break
        if a[l]<0:
            ans+=a[r]
        else:
            ans += (a[l]+a[r]) if l!=r else a[l]
    final.append(str(ans))

stdout.write("\n".join(final))