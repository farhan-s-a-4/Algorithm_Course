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
    b = ILI()
    
    vals = sorted(list(set(a + b)))
    low = 0
    high = len(vals) - 1
    ans = vals[0]
    
    while low <= high:
        mid = (low + high) // 2
        X = vals[mid]
        
        K = 0
        N0 = 0
        zero = False
        
        for i in range(n):
            if a[i] >= X and b[i] >= X:
                K += 1
                if zero:
                    N0 += 1
                zero = False
            elif a[i] < X and b[i] < X:
                zero = True
                
        if zero:
            N0 += 1
        if K >= N0 + 1:
            ans = X
            low = mid + 1
        else:
            high = mid - 1
            
    final.append(str(ans))

stdout.write("\n".join(final) + "\n")