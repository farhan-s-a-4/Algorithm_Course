from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())

final = 0
n = II()
while n > 3:
    n = (n+1)//2
    final += 1
    
stdout.write(f"{final + n}")