import sys

input_data = sys.stdin.read().split()
t = int(input_data[0])
idx = 1
out = []
for _ in range(t):
    n = int(input_data[idx])
    m = int(input_data[idx+1])
    idx += 2
    a = [int(x) for x in input_data[idx:idx+n]]
    idx += n
    b = [int(x) for x in input_data[idx:idx+m]]
    idx += m
    odd_vals = sorted(a[0::2], reverse=True)
    even_vals = sorted(a[1::2], reverse=True)
    c_odd = 0
    c_even = 0
    for x in b:
        if x % 2 != 0:
            c_odd += 1
        else:
            c_even += 1
    marked_sum = 0
    if c_odd > 0 and odd_vals:
        marked_sum += odd_vals[0]
        for i in range(1, min(c_odd, len(odd_vals))):
            if odd_vals[i] > 0:
                marked_sum += odd_vals[i]
            else:
                break
    if c_even > 0 and even_vals:
        marked_sum += even_vals[0]
        for i in range(1, min(c_even, len(even_vals))):
            if even_vals[i] > 0:
                marked_sum += even_vals[i]
            else:
                break
    unmarked_sum = sum(a) - marked_sum
    out.append(str(unmarked_sum))
sys.stdout.write('\n'.join(out) + '\n')