from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().strip().split())
def ILI():
    return list(map(int, stdin.readline().strip().split()))

final = []
for _ in range(II()):
    n, m = IMI()
    a = sorted(ILI(), reverse=True)
    b = sorted(ILI())
    ind = -1
    for i in b:
        ind += i
        if ind > n:
            break
        a[ind] = 0
    final.append(str(sum(a)))
stdout.write('\n'.join(final))