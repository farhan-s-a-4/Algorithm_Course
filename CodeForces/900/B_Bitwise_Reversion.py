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
    x, y, z = IMI()
    a = x | z
    b = x | y
    c = y | z
    if a & b == x and b & c == y and c & a == z:
        final.append("YES")
    else:
        final.append("NO")

stdout.write("\n".join(final))