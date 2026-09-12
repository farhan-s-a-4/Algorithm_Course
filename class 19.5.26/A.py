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
    def count(a, b):
        if (a & 1) == 1 and (b & 1) == 1:
            final.append(str((a*b)+1))
        else:
            final.append(str(((a*b)//2)+2))
    if (n & 1) == 0 and (m & 1) == 1:
        final.append(str(-1))
        continue
    elif(n & 1) == 1 and (m & 1) == 0 and (m % 4) != 0:
        final.append(str(-1))
        continue
    else:
        count(n,m)
        continue
stdout.write("\n".join(final))