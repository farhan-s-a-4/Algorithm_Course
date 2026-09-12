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
    child = []
    for i,v in enumerate(a):
        child.append([v, i+2])
    child.sort(key = lambda x: (x[0], x[1]))

    m = II()
    b = ILI()
    d = [0]*(n+1)
    for i in b:
        d[i] = 1

    count = 0
    ans = []
    for p, c in child:
        if d[p] in [0,1] and d[c] == 1:
            d[c] = -1
            count += 1
            ans.append(str(c))
            
    final.append(str(count) + " " + " ".join(ans))

stdout.write("\n".join(final))