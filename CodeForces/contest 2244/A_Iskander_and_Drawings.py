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
    s = SI()
    m = 0
    c = 0
    for i in s:
        if i == "#":
            c+=1
        else:
            m=max(m, c)
            c=0
    m = max(m, c)
    final.append(str((m+1)//2))

stdout.write("\n".join(final))