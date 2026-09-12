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

final = [0, 0, 0]
for _ in range(II()):
    x, y, z = IMI()
    final[0] += x
    final[1] += y
    final[2] += z

stdout.write("YES" if all(x == 0 for x in final) else "NO")