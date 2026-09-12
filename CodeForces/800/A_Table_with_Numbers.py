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
    n, h, l = IMI()
    a = sorted(ILI())
    if h > l:
        h, l = l, h
    i = 0
    j = n - 1
    while j >= 0 and a[j] > l:
        j -= 1
    ans = 0
    while i < j and a[i] <= h:
        i += 1
        j -= 1
        ans += 1

    final.append(str(ans))

stdout.write("\n".join(final))