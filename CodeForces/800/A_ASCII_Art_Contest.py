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

  
n1, n2, n3 = IMI()
if max([n1, n2, n3]) - min([n1, n2, n3]) >= 10:
    stdout.write("check again")
else:
    stdout.write(f"final {sorted([n1, n2, n3])[1]}")
