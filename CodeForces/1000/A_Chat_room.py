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

final = "hello"
s = SI()
pos = 0
for i in s:
    if i == final[pos]:
        pos+=1
        if pos >= 5:
            break
stdout.write("YES" if pos >= 5 else "NO")