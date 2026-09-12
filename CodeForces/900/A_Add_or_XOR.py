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
    a, b, x, y = IMI()
    if a > b:
        final.append(str(y if (a ^ 1) == b else -1))
    else:
        c0 = b - a
        c1 = ((b + 1) // 2) - ((a + 1) // 2)
        if y > x:
            final.append(str(c0 * x))
        else:
            final.append(str((c0 - c1) * x + c1 * y))

stdout.write("\n".join(final))