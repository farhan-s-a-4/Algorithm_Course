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
    l = ILI()
    c = 0
    for i in range(n):
        a = l[i]
        b = m
        nd = a & b
        r = a | b
        if nd > r:
            x = nd
        else:
            x = r
        if x > c:
            c = x
    print(c)

stdout.write("\n".join(final))