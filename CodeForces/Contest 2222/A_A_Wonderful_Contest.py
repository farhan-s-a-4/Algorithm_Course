from sys import stdin, stdout
def II():
    return int(stdin.readline())
def ISI():
    return set(map(int, stdin.readline().split()))
 
final = []
for _ in range(II()):
    n = II()
    a = ISI()
    if 100 in a:
        final.append("Yes")
    else:
        final.append("No")
stdout.write("\n".join(final))