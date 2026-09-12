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
    s = SI()
    c4 = s.count("4")
    sn = [ch for ch in s if ch != '4']
    total13 = sum(1 for ch in sn if ch in '13')
    left2 = 0
    right_13 = total13
    maxim = left2 + right_13 
    for c in sn:
        if c == '2':
            left2 += 1
        else:
            right_13 -= 1
        if left2 + right_13 > maxim:
            maxim = left2 + right_13
    r123 = len(sn) - maxim
    final.append(str(c4 + r123))
stdout.write("\n".join(final))