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
    a = SI()
    m = II()
    b = SI()
    c = SI()
    v, d = [], []
    for i in range(m):
        if c[i] == 'V':
            v.append(b[i])
        else:
            d.append(b[i])
    final.append("".join(v[::-1]) + a + "".join(d))
stdout.write("\n".join(final))