from sys import stdin, stdout

def readall():
    return stdin.read().split()
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

a = list(map(int, readall()))
ans = sum(a)
ans = max(a[0]*a[1]*a[2], ans)
ans = max((a[0]+a[1])*a[2], ans)
ans = max(a[0]*(a[1]+a[2]), ans)
stdout.write(str(ans))