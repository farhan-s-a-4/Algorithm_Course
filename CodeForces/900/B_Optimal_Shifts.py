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
    if '0' not in s:
        final.append('0')
        continue
    first_one = s.find('1')
    s = s[first_one:] + s[:first_one]
    
    max_zeros = 0
    current_zeros = 0
    
    for char in s:
        if char == '0':
            current_zeros += 1
            if current_zeros > max_zeros:
                max_zeros = current_zeros
        else:
            current_zeros = 0
            
    final.append(str(max_zeros))

stdout.write("\n".join(final))