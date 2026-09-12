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
    a = ILI()
    curr = None
    possible = True
    for i in range(n):
        if i < n-2:
            if a[i] > a[i+1]:
                if curr is None:
                    curr = a[i+2] - a[i+1]
                    if i!=0 and curr <= 0:
                        possible = False
                        break
                elif curr != a[i+2] - a[i+1]:
                    possible = False
                    break
        elif i == n-2:
            if a[i] > a[i+1]:
                if curr is None:
                    curr = a[i] - a[i+1]
                elif curr < a[i] - a[i+1]:
                    possible = False
                    break

    if possible:
        final.append("YES")
    else:
        final.append("NO")
                
stdout.write("\n".join(final))