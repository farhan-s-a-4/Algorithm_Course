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
    ans = "YES"
    for i in range(1, n-1, 1):
        if a[i] < a[i-1] and a[i] < a[i+1]:
            ans = "NO"
            break
    final.append(ans)

stdout.write("\n".join(final))