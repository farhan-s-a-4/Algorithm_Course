from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().strip().split()))

final = []
for _ in range(II()):
    n = II()
    a = sorted(ILI())
    l, r = 0, n - 1
    length = 0
    while l <= r:
        if (a[l]+a[r]) & 1:
            l += 1
        else:
            length = r - l + 1
            break
    l, r = 0, n - 1
    while l <= r:
        if (a[l]+a[r]) & 1:
            r -= 1
        else:
            length = max(length, (r - l + 1))
            break
    final.append(str(n-length))
stdout.write("\n".join(final))
