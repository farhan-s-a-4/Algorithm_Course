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
    return list(SI())

final = []
for _ in range(II()):
    n, m = IMI()
    s = SLI()
    ones = [i for i, v in enumerate(s) if v == "1"]
    if not ones:
        final.append("0")
        continue
    count = 1
    for i in range(len(ones) - 1):
        if ones[i+1] - ones[i] >= m:
            count += 1
    final.append(str(count))

stdout.write("\n".join(final))