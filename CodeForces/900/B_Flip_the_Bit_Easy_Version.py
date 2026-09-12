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
    n, k = IMI()
    a = ILI()
    p = II()
    p -= 1
    val = a[p]

    r, l = 0, 0
    
    prev = val
    for i in range(p , n):
        if prev != a[i]:
            prev = a[i]
            r += 1

    prev = val
    for i in range(p, -1, -1):
        if a[i] != prev:
            l += 1
            prev = a[i]

    mx = max(l,r)
    if mx%2 == 0:
        final.append(str(mx))
    else:
        final.append(str(mx+1))

stdout.write("\n".join(final))