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
    if sum(a) == 1:
        final.append("NO")
        continue
    s = abs(sum(a))
    if s==0 or (s % 4 == 0):
        final.append("YES")
    else:
        final.append("NO")
stdout.write("\n".join(final))