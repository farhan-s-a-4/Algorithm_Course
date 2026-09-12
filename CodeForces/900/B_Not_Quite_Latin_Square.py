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
    string = [SI() for x in range(3)]
    for s in string:
        if '?' in s:
            final += [c for c in ['A', 'B', 'C'] if c not in s]

stdout.write("\n".join(final))