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
    b = ILI()
    if (a[0]+n-1) < (b[0]+m-1):
        final.append("2")
    else:
        final.append("1")

stdout.write("\n".join(final))