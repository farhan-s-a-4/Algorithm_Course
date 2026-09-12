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
    zero = [i for i, x in enumerate(a) if x == 0]
    x, y = zero[0], zero[1]
    z = (x+y)
    z1, z2 = z//2, -1
    if z&1 == 1:
        z2 = z1+1
    else:
        z2 = z1
    def get(l, r):
        seen = set()
        while l >= 0 and r < 2*n:
            if a[l] == a[r]:
                seen.add(a[l])
            else:
                break
            l -= 1
            r += 1
        mex = 0
        while mex in seen:
            mex+=1
        return mex
    ans = max(get(x, x), get(y, y), get(z1, z2))
    final.append(f"{ans}")

stdout.write("\n".join(final))