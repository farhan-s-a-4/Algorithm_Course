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
    a, b, c = IMI()
    if a == b:
        final.append(str(c))
    elif a == c:
        final.append(str(b))
    else:
        final.append(str(a))

stdout.write("\n".join(final))