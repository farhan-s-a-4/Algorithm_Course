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

final = [
    4, 7,
    44, 74, 47, 77,
    444, 744, 474, 774, 447, 747, 477, 777]
n = II()
stdout.write("YES" if any(n%x == 0 for x in final) else "NO")