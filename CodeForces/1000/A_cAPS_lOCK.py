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

s = SI()
if len(s) == 1 and s.islower():
    s = s.upper()
elif s[0].islower() and s[1:].isupper():
    s = s[0].upper() + s[1:].lower()
elif (s.isupper()):
    s = s.lower()
stdout.write(s)