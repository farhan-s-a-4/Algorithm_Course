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
n = []
maxi = 0
for _ in range(II()):
    n.append(II())
    maxi = max(maxi, n[-1])
    
a = [1,2] + [3 * 2**i for i in range(maxi-1)]

for i in n:
    if i == 2:
        final.append("1 2")
    final.append(" ".join(map(str, a[:i])))

stdout.write("\n".join(final))