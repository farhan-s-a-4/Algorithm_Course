from sys import stdin, stdout
import itertools

def II():
    return int(stdin.readline().strip())
def IMI():
    return map(int, stdin.readline().strip().split())
def ILI():
    return list(map(int, stdin.readline().strip().split()))
def SLI():
    return stdin.readline().split()


def find_largest_leq(a_str, d):
    L = len(a_str)

    def backtrack(pos, tight, current):
        if pos == L:
            return int("".join(map(str, current)))
        limit = int(a_str[pos]) if tight else 9
        for dig in reversed(d):
            if dig > limit:
                continue
            if pos == 0 and L > 1 and dig == 0:
                continue
            if not (tight and dig == limit):
                rest = [d[-1]] * (L - pos - 1)
                return int("".join(map(str, current + [dig] + rest)))
            else:
                result = backtrack(pos + 1, True, current + [dig])
                if result is not None:
                    return result
        return None

    return backtrack(0, True, [])

def find_smallest_geq(a_str, d):
    L = len(a_str)

    def backtrack(pos, tight, current):
        if pos == L:
            return int("".join(map(str, current)))
        limit = int(a_str[pos]) if tight else 0
        for dig in d:
            if tight and dig < limit:
                continue
            if pos == 0 and L > 1 and dig == 0:
                continue
            if not (tight and dig == limit):
                rest = [d[0]] * (L - pos - 1)
                return int("".join(map(str, current + [dig] + rest)))
            else:
                result = backtrack(pos + 1, True, current + [dig])
                if result is not None:
                    return result
        return None

    return backtrack(0, True, [])

final = []
for _ in range(II()):
    a_str, n = SLI()
    a = int(a_str)
    n = int(n)
    d = ILI()

    best = float('inf')
    L = len(a_str)
    non_zero = [x for x in d if x != 0]

    for length in [L - 1, L, L + 1]:
        if length <= 0:
            continue

        if length == 1:
            for dig in d:
                best = min(best, abs(a - dig))
            continue

        if not non_zero:
            continue

        if length != L:
            small_val = int(str(non_zero[0]) + str(d[0]) * (length - 1))
            large_val = int(str(d[-1]) * length)
            best = min(best, abs(a - small_val), abs(a - large_val))
        else:
            res = find_largest_leq(a_str, d)
            if res is not None:
                best = min(best, abs(a - res))
            res = find_smallest_geq(a_str, d)
            if res is not None:
                best = min(best, abs(a - res))

    if 0 in d:
        best = min(best, a)

    final.append(best)

stdout.write("\n".join(map(str, final)) + "\n")