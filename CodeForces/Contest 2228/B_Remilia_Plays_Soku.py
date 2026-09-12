from sys import stdin, stdout
def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().strip().split())

final = []
for _ in range(II()):
    n, x,y = int(next(it))
    m = int(next(it))
    
    if x == y:
        final.append(str(0))
        continue
        
    if n <= 3:
        final.append(str(1))
        continue
        
    ans = min(abs(x - y), n - abs(x - y)) + m
    final.append(str(ans))
    
stdout.write('\n'.join(final) + '\n')

