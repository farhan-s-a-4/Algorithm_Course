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
    b = ILI()
    second = -1
    ans = 0
    for i in range(n):
        second = max(second, min(a[i], b[i]))
        ans += max(a[i], b[i])
    ans += second
    final.append(str(ans))

stdout.write("\n".join(final))