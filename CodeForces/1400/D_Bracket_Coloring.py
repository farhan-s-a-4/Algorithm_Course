from sys import stdin, stdout
from math import inf

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))

final = []
for _ in range(II()):
    n = II()
    s = stdin.readline().strip()

    if 2 * s.count("(") != n:
        final.append("-1")
        continue
    
    plus = s[0]
    X = []
    Y = []

    for i, char in enumerate(s):
        if char == plus:
            X.append(i)
        else:
            if X:
                X.pop()
            else:
                Y.append(i)
        
    if not X and not Y:
        final.append("1")
    else:
        final.append("2")
   
    col = ["1"] * n
    for lst in [X, Y]:
        for i in lst:
            col[i] = "2"
    
    final.append(" ".join(col))

stdout.write("\n".join(final))