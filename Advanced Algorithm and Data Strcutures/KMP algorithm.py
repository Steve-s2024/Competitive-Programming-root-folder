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