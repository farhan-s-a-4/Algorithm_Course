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
    n, l, r = IMI()
    a = ILI()
    final.append(str(min(sum(sorted(x)[:r-l+1]) for x in (a[:r], a[l-1:]))))

stdout.write("\n".join(final))
