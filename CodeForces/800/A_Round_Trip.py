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
    R, X, D, n = IMI()
    string = SI()
    count = 0
    for i in range(n):
        if string[i] == '2':
            if R<X:
                R -= D
                count += 1
        else:
            R -= D
            count += 1
    final.append(str(count))

stdout.write("\n".join(final))