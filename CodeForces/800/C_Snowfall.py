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
    n=II()
    a = ILI()
    a6, a2, a3, a_other = [], [], [], []
    for x in a:
        if x%6 == 0:
            a6.append(x)
        elif x%2 == 0:
            a2.append(x)
        elif x%3 == 0:
            a3.append(x)
        else:
            a_other.append(x)
    final.append(" ".join(map(str, a6+a2+a_other+a3)))

stdout.write("\n".join(final))