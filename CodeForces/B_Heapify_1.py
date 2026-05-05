from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int,stdin.readline().split()))

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    for i in range(1, (n+1)//2+1, 2):
        j = i
        b = []
        while j <= n:
            b.append(a[j-1])
            j *= 2
        b.sort()
        j = i
        for x in b:
            a[j-1] = x
            j *= 2
    issorted = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            issorted = False
            break
    final.append("YES" if issorted else "NO")

stdout.write('\n'.join(final))