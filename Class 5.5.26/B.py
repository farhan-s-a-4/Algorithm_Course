from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def SI():
    return stdin.readline().strip()

final = []
for _ in range(II()):
    n = II()
    s = SI()
    stack = []
    for b in s:
        if stack and stack[-1] != b:
            stack.pop()
        else:
            stack.append(b)
    final.append("YES" if not stack else "NO")

stdout.write("\n".join(final))