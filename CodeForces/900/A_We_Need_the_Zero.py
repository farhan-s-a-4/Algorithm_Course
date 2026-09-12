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
    x = 0
    for i in a:
        x = x ^ i
    if n%2 == 1:
        final.append(str(x))
    else:
        if x==0:
            final.append(str(x))
        else:
            final.append(str(-1))

stdout.write("\n".join(final))