from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().strip().split()))
final = []
for _ in range(II()):
    n = II()
    L = ILI()
    ans = 0
    for i in range(n - 1):
        ans += 1 if L[i] % (L[i + 1] - L[i]) == 0 else 0
    final.append(str(ans))
stdout.write('\n'.join(final))