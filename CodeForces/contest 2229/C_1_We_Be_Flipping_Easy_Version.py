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
    
    ops = []
    flip = False
    
    for i in range(n - 1, -1, -1):
        current_val = -a[i] if flip else a[i]
        if current_val > 0:
            ops.append(str(i + 1))
            flip = not flip
            
    final.append(str(len(ops)))
    if ops:
        final.append(" ".join(ops))
    else:
        final.append("")
            
stdout.write("\n".join(final))