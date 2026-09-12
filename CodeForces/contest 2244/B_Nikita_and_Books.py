from sys import stdin, stdout

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
    req, cur = 0, 0
    for i in range(n):
        req += (i+1)
        cur += a[i]
        if cur < req:
            final.append("NO")
            break
    else:
        final.append("YES")

stdout.write("\n".join(final))