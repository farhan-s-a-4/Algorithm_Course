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
    n,m=IMI()
    ans1, ans2 = [], []
    for j in range(m):
        ans1.append('1' if (j%4==1)or(j%4==2) else '0')
        ans2.append('0' if (j%4==1)or(j%4==2) else '1')
        
    s1 = " ".join(ans1)
    s2 = " ".join(ans2)
        
    for i in range(n):
        final.append((s1 if (i%4==1)or(i%4==2) else s2) )

stdout.write("\n".join(final))