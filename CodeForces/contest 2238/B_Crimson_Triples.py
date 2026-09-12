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
    
    total = 0
    for i in range(1,n+1):
        temp = n // i
        total += temp * temp
        
    final.append(str(total))

stdout.write("\n".join(final))