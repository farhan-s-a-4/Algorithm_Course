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

final = 0
n, m = IMI()
a = ILI()
for i in range(m-1):
    if a[i] > a[i+1]:
        final += 1
final *= n
final += a[-1] - 1

stdout.write(str(final))