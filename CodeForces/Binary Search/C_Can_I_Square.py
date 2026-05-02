from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().split()))

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    total = sum(a)
    l, r = 1, 10**8
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == total:
            final.append('YES')
            break
        elif mid * mid < total:
            if (mid + 1) * (mid + 1) > total:
                final.append('NO')
                break
            l = mid + 1
        else:
            r = mid - 1
for result in final:
    stdout.write(result + '\n')