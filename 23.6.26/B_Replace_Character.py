from sys import stdin, stdout
from collections import Counter

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))
def SI():
    return stdin.readline().strip()
def SLI():
    return list(SI())

final = []
for _ in range(II()):
    n = II()
    s= SLI()
    letters = Counter(s)

    sorted_ = dict(sorted(letters.items(), key= lambda item: (item[1], item[0])))
    ans = list(sorted_)
    s[s.index(ans[0])] = s[s.index(ans[-1])]

    final.append("".join(s))

stdout.write("\n".join(final))