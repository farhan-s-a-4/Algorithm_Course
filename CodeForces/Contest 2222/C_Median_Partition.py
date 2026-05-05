from sys import stdin, stdout

def II():
    return int(stdin.readline().strip())
def ILI():
    return list(map(int, (stdin.readline().split())))

for _ in range(II()):
    n = II()
    a = ILI()
    sorted_a = sorted(a)
    median = sorted_a[n // 2]

    px = [0] * (n + 1)
    py = [0] * (n + 1)
    
    for i in range(n):
        px[i+1] = px[i] + (1 if a[i] >= median else -1)
        py[i+1] = py[i] + (1 if a[i] <= median else -1)

    dp = [-1] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(i - 1, -1, -2):
            if dp[j] != -1:
                if px[i] > px[j] and py[i] > py[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
    print(dp[n])