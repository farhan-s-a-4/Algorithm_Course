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
    i = 1
    while n % i == 0:
        i += 1
        
    final.append(str(i - 1))
    

stdout.write("\n".join(final))