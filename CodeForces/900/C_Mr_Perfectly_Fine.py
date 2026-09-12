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
    skills = {'11': float('inf'), '10': float('inf'), '01': float('inf')}
    for i in range(n):
        p, s = SLI()
        if s in ['11', '10', '01']:
            skills[s] = min(skills[s], int(p))
    final.append(str(min(skills['11'], skills['10'] + skills['01'])) if min(skills['11'], skills['10'] + skills['01']) != float('inf') else '-1')

stdout.write("\n".join(final))