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
    n, k = IMI()
    a = list(map(int, SLI()))
    if 1 in a :
        idx=a.index(1)
        if 1 in a[idx+k:]:
            print("NO") 
            continue
    print("YES")

stdout.write("\n".join(final))