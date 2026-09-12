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
    n, m = IMI()
    v = ILI()
    all_vals = []
    for __ in range(n):
        all_vals += ILI()

    unique_vals = sorted(set(all_vals))
    U = len(unique_vals)
    val_to_idx = {val: i for i, val in enumerate(unique_vals)}

    bit_sum = [0] * (U + 1)
    bit_cnt = [0] * (U + 1)
    LOG = U.bit_length()

    total_sum = 0
    ans = m

    for k in range(n - 1, -1, -1):
        row_start = k * m
        for c in range(m):
            val = all_vals[row_start + c]
            pos = U - val_to_idx[val]
            total_sum += val
            while pos <= U:
                bit_sum[pos] += val
                bit_cnt[pos] += 1
                pos += pos & (-pos)

        target = v[k]
        if target <= 0:
            ans = 0
            continue
        if total_sum < target:
            continue

        pos = 0
        cur_sum = 0
        cur_cnt = 0
        for pw in range(LOG, -1, -1):
            npos = pos + (1 << pw)
            if npos <= U and cur_sum + bit_sum[npos] < target:
                pos = npos
                cur_sum += bit_sum[pos]
                cur_cnt += bit_cnt[pos]

        remaining = target - cur_sum
        if pos < U:
            val_next = unique_vals[U - 1 - pos]
            needed = -(-remaining // val_next)
            pieces = cur_cnt + needed
        else:
            pieces = cur_cnt

        if pieces < ans:
            ans = pieces

    final.append(str(ans))

stdout.write("\n".join(final))