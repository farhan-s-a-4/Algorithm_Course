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
    a = sorted(ILI(), reverse=True)
    b = sorted(ILI())
    curr = -1
    for i in b:
        curr += i
        if curr >= n:
            break
        a[curr] = 0
    final.append(f"{sum(a)}")

stdout.write("\n".join(final))