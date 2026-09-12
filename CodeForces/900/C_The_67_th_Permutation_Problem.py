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
    i = 1
    j = 3 * n
    perm = []
    
    while i <= j:
        # U3-L2: Each block: small, median, large
        perm.append(i)
        perm.append(j - 1)
        perm.append(j)
        # U3-L3: Move pointers
        i += 1
        j -= 2
    
    final.append(' '.join(map(str, perm)))
    
stdout.write('\n'.join(final))