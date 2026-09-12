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
    l, sl, d = IMI()
    if d<sl:
        final.append("NO")
        continue
    a = [1]*(sl-1) + [d-sl+1]
    final.append("YES")
    final.append(" ".join(map(str, (a * (l // sl + 1))[:l])))

stdout.write("\n".join(final))