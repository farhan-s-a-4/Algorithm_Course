def lcsRec(s1, s2, m, n):
    if m == 0 or n == 0:
        return ""
    if s1[m - 1] == s2[n - 1]:
        return s1[m - 1] + lcsRec(s1, s2, m - 1, n - 1)

    else:
        lcs1 = lcsRec(s1, s2, m, n - 1)
        lcs2 = lcsRec(s1, s2, m - 1, n)
        if len(lcs1) > len(lcs2):
            return lcs1
        else:
            return lcs2

def lcs(s1,s2):
    m = len(s1)
    n = len(s2)
    return lcsRec(s1,s2,m,n)

if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print((ans := lcs(s1, s2))[::-1])
