from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().split()))

final = []
n = II()
a = sorted(ILI())
for i in range(II()):
    q = II()
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == q or a[mid] < q:
            if mid == n - 1:
                final.append(str(mid + 1))
                break
            l = mid + 1
        else:
            if mid == 0:
                final.append('0')
                break
            elif a[mid - 1] <= q:
                final.append(str(mid))
                break
            r = mid - 1
stdout.write('\n'.join(final) + '\n')