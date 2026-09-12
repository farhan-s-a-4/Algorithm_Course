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
    ans1 = a[0]%3
    sum1 = sum(a[1:])
    sum2 = 0
    found = False
    for i in range(n-1, 1, -1):
        sum1 -= a[i]
        sum2 += a[i]
        temp1 = sum1%3
        temp2 = sum2%3
        if (temp1 != temp2 and temp2 != ans1 and temp1 != ans1):
            final.append("1 " + str(i))
            found = True
            break
        if(temp1==temp2 and temp1==ans1):
            final.append("1 " + str(i))
            found = True
            break
    if not found:
        final.append("0 0")

stdout.write("\n".join(final))
