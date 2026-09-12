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
    a = []
    for i in range(1, n + 1, 2):
        a.append(i+1)
        a.append(i)
    final.append(" ".join(map(str, a)))

stdout.write("\n".join(final))