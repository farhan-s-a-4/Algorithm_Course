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

for i in range(II()):
    s = SI()
    n = len(s)
    found = False
    
    for val in [[-1, 1, 1], [-1, -1, 1], [-1, 1, -1], [1, -1, 1], [1, -1, -1], [1, 1, -1]]:
        x = 0
        for c in s:
            if c == 'A':
                x += val[0]
            elif c == 'B':
                x += val[1]
            else:
                x += val[2]
            if x < 0:
                break
        if x == 0:
            found = True
            break
    final.append("YES" if found else "NO")

stdout.write("\n".join(final))