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
    a = ILI()
    b = sorted(ILI())
    prev, cur = 0, b[0]
    total = abs(sum(a[:cur]))
    for i in b[1:]:
        prev, cur = cur, i
        total += abs(sum(a[prev:cur]))
    
    if cur < n:
        total += (sum(a[cur:]))

    final.append(str(total))

stdout.write("\n".join(final))