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
    s = SI()
    max_d = d = 0
    for c in s:
        if c == "L":
            d += 1
        else:
            max_d = max(max_d, d)
            d = 0
    max_d = max(max_d, d)
    final.append(str(max_d + 1))

stdout.write("\n".join(final))