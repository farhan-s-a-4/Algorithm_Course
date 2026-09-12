from sys import stdin, stdout
import math

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().split())
def ILI():
    return list(map(int, stdin.readline().split()))

def build_sparse(a):
    n = len(a)
    LOG = math.floor(math.log2(n)) + 1
    st = [a[:]]
    for j in range(1, LOG):
        prev = st[-1]
        curr = []
        length = 1 << j
        half = length >> 1
        for i in range(n - length + 1):
            curr.append(prev[i] & prev[i + half])
        st.append(curr)
    return st

def range_and(st, l, r):
    length = r - l + 1
    j = length.bit_length() - 1
    return st[j][l] & st[j][r - (1 << j) + 1]

final = []
for _ in range(II()):
    n = II()
    a = ILI()
    st = build_sparse(a)
    
    q = II()
    answers = []
    for _ in range(q):
        l, k = IMI()
        l -= 1
        if a[l] < k:
            answers.append("-1")
            continue
            
        left = l
        right = n - 1
        ans = l
        while left <= right:
            mid = (left + right) // 2
            if range_and(st, l, mid) >= k:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        answers.append(str(ans + 1))
        
    final.append(" ".join(answers))

stdout.write("\n".join(final))
