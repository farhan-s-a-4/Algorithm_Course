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
    s = SI()
    c1 = 0
    c2 = 0
    curr = 0
    for i in range(n):
        if s[i] == '<':
            c1 += 1
            c2 = 0
            curr = max(curr, c1)
        if s[i] == '>':
            c2 += 1
            c1 = 0
            curr = max(curr, c2)
            
    final.append(str(curr + 1))

stdout.write("\n".join(final))