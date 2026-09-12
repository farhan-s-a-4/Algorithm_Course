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
    cmax = -1
    add = 0
    for x in a:
        add = max(add, cmax - x)
        cmax = max(cmax, x)
    curr = -1
    unpossible = False
    for x in a:
        if x < curr:
            x += add
            if x < curr:
                unpossible = True
                break
        curr = x
    final.append("YNEOS"[unpossible::2])
 
stdout.write("\n".join(final))