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
    return list(stdin.readline().strip())

final = []
for _ in range(II()):
    n = II()
    s = SI()
    if ('01'in s)^('10'in s):
        final.append("2")
    else:
        final.append("1")

stdout.write("\n".join(final))
