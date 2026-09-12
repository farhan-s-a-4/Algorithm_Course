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
    b = ILI()
    cnt11, cnt10, cnt01, cnt00 = 0, 0, 0, 0
    for x, y in zip(a, b):
        if x == 1 and y == 1:
            cnt11 += 1
        elif x == 1 and y == 0:
            cnt10 += 1
        elif x == 0 and y == 1:
            cnt01 += 1
        else:
            cnt00 += 1

    if cnt10 == 0 and cnt01 == 0:
        final.append("0")
        continue
    if cnt10 % 2:
        final.append("1")
        continue
    if cnt10 > 0:
        final.append("2")
        continue
    if cnt01 != 0 and cnt11 > 0 and cnt00 > 0:
        final.append("2")
        continue
    final.append("-1")

stdout.write("\n".join(final))