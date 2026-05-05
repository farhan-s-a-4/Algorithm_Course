from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().strip().split()))

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    b = ILI()
    ind = [[-1]]*(n+1)
    for i, v in enumerate(b):
        print(i, v)
        ind[v].append(i)
        print(ind[v])
    print(ind)