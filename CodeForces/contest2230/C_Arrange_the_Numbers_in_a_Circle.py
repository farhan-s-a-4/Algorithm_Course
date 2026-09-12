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
    
    one = 0
    not1 = []
    
    for i in a:
        if i == 1:
            one += 1
        elif i >= 2:
            not1.append(i)
            
    if len(not1) == 0:
        total = 0
    elif len(not1) == 1:
        base = not1[0]
        slots = base // 2
        total = base + min(one, slots)
    else:
        base = sum(not1)
        slots = sum((x // 2) - 1 for x in not1)
        total = base + min(one, slots)
        
    if total < 3:
        final.append("0")
    else:
        final.append(str(total))
stdout.write("\n".join(final))