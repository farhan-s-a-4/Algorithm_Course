from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().strip().split()))

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    a0, a1, a2 = 0, 0, 0
    for i in a:
        if i == 0:
            a0 += 1
        elif i == 1:
            a1 += 1
        else:
            a2 += 1
    ans = a0 + min(a1, a2)
    if a1 > a2:
        ans += (a1 - a2) // 3
    else:
        ans += (a2 - a1) // 3
    final.append(ans)

stdout.write('\n'.join(map(str, final)))