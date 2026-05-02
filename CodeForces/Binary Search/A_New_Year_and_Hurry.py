from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
time = 240 - m
if time <= 4:
    stdout.write('0')
    exit()
prob = [i*5 for i in range(1, n+1)]
for i in range(1, n):
    prob[i] += prob[i-1]
l, r = 0, n-1
while l <= r:
    if l == r:
        if prob[l] <= time:
            stdout.write(str(l + 1))
        else:
            stdout.write(str(l))
        break
    mid = (l + r) // 2
    if prob[mid] == time:
        stdout.write(str(mid + 1))
        break
    elif prob[mid] < time:
        if mid < n-1 and prob[mid + 1] > time:
            stdout.write(str(mid + 1))
            break
        l = mid + 1
    else:
        r = mid - 1