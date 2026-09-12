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
    return set(stdin.readline().lower().strip())

final = []
for _ in range(II()):
    n, m = IMI()
    a = set()
    b = set()
    for i in range(n):
        s = SI()[0]
        a.add(s)
    for i in range(m):
        s = set(SLI())
        b = b | s

    final.append("YNEOS"[(a|b!=a)::2])


stdout.write("\n".join(final))