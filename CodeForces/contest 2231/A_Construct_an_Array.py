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
    lim = 750
    allowed = [True]*lim
    num = []
    def function():
        curr = -1
        for i in range(1, lim):
            if i == 1:
                num.append(i)
                curr = i
                continue
            else:
                if allowed[i] and i+curr < lim:
                    num.append(i)
                    allowed[i+curr] = False
                    curr = i
                elif allowed[i]:
                    num.append(i)
                    curr = i
    function()
    n = II()
    final.append(" ".join(map(str, num[:n])))

stdout.write("\n".join(final))