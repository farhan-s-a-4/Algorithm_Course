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

s, n = IMI()
a = [ILI() for _ in range(n)]
a.sort()
pos = True
for x in a:
    if s > x[0]:
        s += x[1]
    else:
        pos = False
        break
stdout.write("YES" if pos else "NO")