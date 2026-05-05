from sys import stdin, stdout

def II(): 
    return int(stdin.readline().strip())

def ILI(): 
    return list(map(int, stdin.readline().split()))

final = []
for _ in range(II()):
    n = II()
    p = ILI()
    c = ILI()
    pind = [0] * (n + 1)
    for i, val in enumerate(p):
        pind[val] = i
    ans = "YES"
    last = -1
    for val in c:
        curr = pind[val]
        if curr < last:
            ans = "NO"
            break
        last = curr
    final.append(ans)
stdout.write('\n'.join(final) + '\n')