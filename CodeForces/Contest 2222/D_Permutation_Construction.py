from sys import stdin, stdout
 
def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, stdin.readline().split()))
 
final = []
for _ in range(II()):
    n = II()
    a = ILI()
    v = []
    current_sum = 0
    for i in range(n):
        v.append((current_sum, i))
        current_sum += a[i]
    v.sort()
    p = [0] * n
    current_p = n
    for val, original_index in v:
        p[original_index] = current_p
        current_p -= 1
    final.append(" ".join(map(str, p)))
 
stdout.write("\n".join(final) + "\n")