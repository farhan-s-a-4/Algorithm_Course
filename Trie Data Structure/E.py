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
    a, b = SLI()
    a = a[::-1]
    b = b[::-1]
    ap, bp = -1, -1
    for i, v in enumerate(a):
        if v == "P":
            ap = i
            break
    for i, v in enumerate(b):
        if v == "P":
            bp = i
            break
    if ap != bp:
        final.append("NO")
        continue
    else:
        acount, bcount = 0, 0
        for c in a[ap:]:
            if c == "P":
                acount += 1
        if acount == 0:
            if a == b:
                final.append("YES")
            else:
                final.append("NO")
            continue
        for c in b[bp:]:
            if c == "P":
                bcount += 1
        if acount == bcount:
            final.append("YES")
        else:
            final.append("NO")

stdout.write("\n".join(final))