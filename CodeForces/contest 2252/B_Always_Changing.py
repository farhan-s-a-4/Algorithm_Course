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
    s = SI()
    
    c0 = s.count('0')
    c1 = s.count('1')
    D = c0 - c1
    
    if D < -2 or D > 2:
        final.append("-1")
        continue
        
    len_0 = 0
    expected = '0'
    for char in s:
        if char == expected:
            len_0 += 1
            expected = '1' if expected == '0' else '0'
            
    len_1 = 0
    expected = '1'
    for char in s:
        if char == expected:
            len_1 += 1
            expected = '1' if expected == '0' else '0'
            
    if len_0 % 2 == 0:
        type_A = len_0
        type_C = len_0 - 1 if len_0 > 0 else -1
    else:
        type_C = len_0
        type_A = len_0 - 1

    if len_1 % 2 == 0:
        type_B = len_1
        type_D = len_1 - 1 if len_1 > 0 else -1
    else:
        type_D = len_1
        type_B = len_1 - 1
        
    best_len = -1
    
    for D_prime in [-1, 0, 1]:
        if abs(D - D_prime) <= 1:
            if D_prime == 0:
                best_len = max(best_len, type_A, type_B)
            elif D_prime == 1:
                best_len = max(best_len, type_C)
            elif D_prime == -1:
                best_len = max(best_len, type_D)
                
    if best_len >= 0:
        final.append(str(n - best_len))
    else:
        final.append("-1")

stdout.write("\n".join(final))

