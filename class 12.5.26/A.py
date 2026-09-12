from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
final = []
for _ in range(II()):
    n = II()
    ans = n
    while n > 0:
        n >>= 1
        ans += n
    final.append(str(ans))
stdout.write('\n'.join(final))