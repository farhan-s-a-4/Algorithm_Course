from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def SI():
    return stdin.readline().strip()

final = []
for _ in range(II()):
    n = II()
    s = SI()[::-1]
    ans = []
    maxim = n
    minim = 1
    for sign in s:
        if sign == "<":
            ans.append(minim)
            minim += 1
        else:
            ans.append(maxim)
            maxim -= 1
    ans.append(minim)
    final.append(" ".join(map(str, ans[::-1])))
stdout.write("\n".join(final))
