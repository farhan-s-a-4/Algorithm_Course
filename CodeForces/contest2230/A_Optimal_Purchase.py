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
    if a <= 3:
        final.append(str(min(a*b, c)))
    elif 3*b <= c:
        final.append(str(a*b))
    else:
        final.append(str((a//3)*c + min((a%3)*b, c)))

stdout.write("\n".join(final))