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
    s = SI()[::-1]
    found = {0:False, 5:False}
    for i in range(len(s)):
        x = int(s[i])
        if (x == 2 or x == 7) and found[5]:
            final.append(str(i-1))
            break
        if (x == 0 or x == 5) and found[0]:
            final.append(str(i-1))
            break
        if x in [0, 5]:
            found[x] = True
    else:
        final.append(f'{len(s)}')

stdout.write("\n".join(final))