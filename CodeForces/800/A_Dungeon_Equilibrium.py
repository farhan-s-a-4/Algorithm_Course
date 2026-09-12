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
    import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    cnt = [0] * (n + 1)
    for _ in range(n):
        x = int(next(it))
        if 0 <= x <= n:
            cnt[x] += 1
    ans = 0
    ans += cnt[0]
    for x in range(1, n + 1):
        c = cnt[x]
        if c == 0:
            continue
        if c < x:
            ans += c
        else:
            ans += c - x
    out.append(str(ans))
sys.stdout.write("\n".join(out))

stdout.write("\n".join(final))