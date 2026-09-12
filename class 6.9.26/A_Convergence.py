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
    a.sort()
    
    mid = n // 2
    count_left = 0
    count_right = 0
    for i in range(mid):
        if a[i] != a[mid]:
            count_left += 1
    for i in range(mid + 1, n):
        if a[i] != a[mid]:
            count_right += 1
    ans1 = max(count_left, count_right)

    mid2 = (n - 1) // 2
    if mid == mid2:
        ans2 = ans1
    else:
        count_left = 0
        count_right = 0
        for i in range(mid2):
            if a[i] != a[mid2]:
                count_left += 1
        for i in range(mid2 + 1, n):
            if a[i] != a[mid2]:
                count_right += 1
        ans2 = max(count_left, count_right)
    final.append(str(min(ans1, ans2)))


stdout.write("\n".join(final))