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
    m = a[0]
    ans = 0
    for i in range(1,n):
        if m > a[i]:
            ans += 1
        m = max(a[i],m)
    final.append(str(ans))

stdout.write("\n".join(final))