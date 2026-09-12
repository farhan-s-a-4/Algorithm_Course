import sys
from operator import xor

data = sys.stdin.buffer.read().split()
pos = 0
t = int(data[pos])
pos += 1
out = []

for _ in range(t):
    n = int(data[pos])
    pos += 2
    a = list(map(int, data[pos:pos + n]))
    pos += n

    order = sorted(range(n), key=a.__getitem__)
    max_xor = max(map(xor, order, range(n)), default=0)

    if max_xor == 0:
        out.append("0")
    else:
        k = 1 << (max_xor.bit_length() - 1)
        out.append(str(k))

sys.stdout.write("\n".join(out) + "\n")