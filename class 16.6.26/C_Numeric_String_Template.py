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
    m = II()
    ans = ['YES']*m
    for idx in range(m):
        s = SI()
        if len(s)!=n:
            ans[idx] = "NO"
            continue
        x = [None]*26
        for i, c in enumerate(s):
            if x[ord(c) - ord("a")] is None:
                #print(n, s, i, c)
                x[ord(c) - ord("a")] = a[i]
            else:
                if x[ord(c) - ord("a")] != a[i]:
                    ans[idx] = "NO"
                    break
        if ans[idx] == "NO":
            continue
        x = sorted(list(num for num in x if num != None))
        for i in range((len(x)-1)):
            if x[i] == x[i+1]:
                ans[idx] = "NO"

    final.append('\n'.join(ans))

stdout.write("\n".join(final))