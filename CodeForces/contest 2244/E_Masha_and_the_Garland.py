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
    n, m = IMI()
    s = SI()
    c = [0]*(n+1)
    for i in range(1, n):
        c[i+1] = c[i] + (1 if s[i] == s[i-1] else 0)
    for __ in range(m):
        l, r, t = IMI()
        dif = c[r] - c[l]
        if (dif+1)//2 <= t:
            final.append("YES")
        else:
            final.append("NO")

stdout.write("\n".join(final))