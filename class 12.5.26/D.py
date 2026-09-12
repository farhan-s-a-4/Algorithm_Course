from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().strip().split())
def ILI():
    return list(map(int, stdin.readline().strip().split()))
def SI():
    return stdin.readline().strip()
final = []
for _ in range(II()):
    n = II()
    a = SI()
    c1 = a.count('1')
    ans = a[n-c1:].count('0')
    final.append(str(ans))
stdout.write('\n'.join(final))