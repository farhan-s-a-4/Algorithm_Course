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

final = ""
s = SI().lower()
for i in s:
    if i not in ['a', 'e', 'i', 'o', 'u', 'y']:
        final += "."
        final += i
stdout.write(final)