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
    a = n % 12
    if a == 10:
        a += 12
    final.append(f"{a} {n - a}")
    if n < a:
        final[-1] = "-1"

stdout.write("\n".join(final))