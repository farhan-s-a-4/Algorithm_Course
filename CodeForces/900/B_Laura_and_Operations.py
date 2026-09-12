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
    def check(target, num1, num2):
        if num1 & 1 != num2 & 1:
            return "0"
        elif target > 0 or (num1 > 0 and num2 > 0):
            return "1"
        else:
            return "0"
    final.append(check(a, b, c) + " " + check(b, a, c) + " " + check(c, a, b))

stdout.write("\n".join(final))