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
    n=II()
    s=SI()
    c=0
    if '...' in s: c=2
    else: c=s.count('.')
    final.append(str(c))
stdout.write("\n".join(final))