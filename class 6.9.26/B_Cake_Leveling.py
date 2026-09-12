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
    total = 0
    height = 10**9
    result = []
    for i in range(n):
            total += a[i]
            curr = total//(i + 1)
            if curr < height:
                height = curr
            result.append(str(height))
    final.append(" ".join(result))

stdout.write("\n".join(final))