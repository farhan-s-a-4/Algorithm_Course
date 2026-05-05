from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().strip().split()))
final = []
for _ in range(II()):
    n = II()
    a = ILI()
    r = sum(a) - a.count(1)
    if a[-1] == 1:
        r += 1
    final.append(str(r))
stdout.write('\n'.join(final))