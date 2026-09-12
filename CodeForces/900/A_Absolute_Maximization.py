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
    o = 0
    x = a[0]
    for i in a:
        o |= i
        x &= i
    final.append(str(o - x))

stdout.write("\n".join(final))