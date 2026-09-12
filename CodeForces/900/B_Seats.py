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
    n=int(input())
    s=input().strip()
    c=s.count('1')
    l=('10'+s+'01').split('1')
    for zs in l:
        c+=(len(zs)//3)
    print(c)

stdout.write("\n".join(final))