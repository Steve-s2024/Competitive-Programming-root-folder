# this algo is really hard to grasp, it is about sophisticated dp implementation and
# suffix, prefix matching.

# "so, KMP is built on the idea of dp, so if conflict happen when comparing prefix and suffix when building the table,
# it will guarantee to find the longest suffix that is not the conflicting suffix in a short time. and even better is
# that when actually searching for the pattern in the string, the same logic apply, you search for longest matching
# string between target and pattern, and if conflict happens, you use the table to reassign the longest prefix that is
# not the conflicting prefix"



def build(p):
    n = len(p)
    length = 0
    lps = [0] * n
    for i in range(1, n):
        while length > 0 and p[i] != p[length]:
            length = lps[length - 1]
        if p[i] == p[length]:
            length += 1
            lps[i] = length
    print(lps)
    return lps


def check(s, p):
    lps = build(p)
    n = len(s)
    m = len(p)
    j = 0
    for i in range(n):
        while j > 0 and s[i] != p[j]:
            j = lps[j-1]
        if s[i] == p[j]:
            j+=1
        if j == m:
            print(i-m+1, i)
            break

check("aabcadaabe", "cad")
check("aabcadaabe", "z")
check("aabcadaabe", "a")
check("aabcadaabe", "ad")
check("aabcadaabe", "adaabe")




# 2025/08/26
# here is another compact implementation of KMP that returns an array of intervals that represent all the occurrence of
# s2 in s1
def kmp(s1, s2):
    n, m = len(s1), len(s2)
    lps = [0] * m
    l = 0
    for i in range(1, m):
        while s2[i] != s2[l] and l: l = lps[l - 1]
        if s2[i] == s2[l]:
            l += 1
            lps[i] = l
    res = []
    l = 0
    for i in range(n):
        while s1[i] != s2[l] and l: l = lps[l - 1]
        if s1[i] == s2[l]:
            l += 1
            if l == m:
                res.append((i - l + 1, i))
                l = lps[l - 1]
    return res
