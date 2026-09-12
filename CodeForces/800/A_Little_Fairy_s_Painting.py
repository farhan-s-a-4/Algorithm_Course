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
    colors = set(ILI())
    ans = 0
    while True:
        distint = len(colors)
        if distint not in colors:
            colors.add(distint)
        else:
            ans=distint
            break
    final.append(str(ans))

stdout.write("\n".join(final))