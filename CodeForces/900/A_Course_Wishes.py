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
    n, k = IMI()
    a = ILI()
    b = ILI()
    if n*(k+1) - sum(b) > 1000:
        final.append(str(-1))
        continue
    c = sorted(range(n), key=lambda x: b[x], reverse=True)
    steps = []
    for i in c:
        for _ in range(k+1-b[i]):
            steps.append(i+1)
    final.append(str(len(steps)))
    final.append(" ".join(map(str, steps)))

stdout.write("\n".join(final))