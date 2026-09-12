from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))
def SI():
    return stdin.readline().strip()
def SLI():
    return stdin.readline().split()

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    prefmin = [0] * n
    for i in range(n):
        if i == 0:
            prefmin[i] = a[i]
        else:
            prefmin[i] = min(prefmin[i-1], a[i])
    count = 0
    ans = []
    for i in range(n):
        if a[i] > prefmin[i]:
            count += 1
            ans.append(str(i+1))
    final.append(str(count) + '\n' + " ".join(ans))

stdout.write("\n".join(final))