# the algorithm which find the longest palindrome in O(n): Recall that we had the naive way of O(n^2) in solving longest palindrome.


# 2.0 take in string and return the longest palindrome
def manacher(s):
    t = s
    s = '#' + '#'.join(list(s)) + '#'
    n = len(s)

    ar = [0] * n
    c, r = 0, 0
    for i in range(n):
        m = 2 * c - i
        if i <= r and m >= 0: ar[i] = min(r - i, ar[m])
        while i - ar[i] >= 0 and i + ar[i] < n and s[i - ar[i]] == s[i + ar[i]]: ar[i] += 1
        if i + ar[i] >= r: c, r = i, i + ar[i]
    L, R = 0, 0
    for i in range(n):
        x, c = ar[i]//2, i//2
        if s[i] == '#': l, r = c - x, c + x - 1
        else: l, r = c - x+1, c + x-1
        if r-l+1 > R-L+1: L, R = l, r

    return t[L:R+1]




# 1.0, finding the length of the longest palindrome
def manacher(s):
    s = '#' + '#'.join(list(s)) + '#'
    n = len(s)

    ar = [0]*n
    c, r = 0, 0
    for i in range(n):
        m = 2*c-i
        if i <= r and m >= 0: ar[i] = min(r-i, ar[m])
        while i-ar[i] >= 0 and i+ar[i] < n and s[i-ar[i]] == s[i+ar[i]]: ar[i] +=1
        if i+ar[i] >= r: c, r = i, i+ar[i]
    res = 0
    for i in range(n):
        if s[i] == '#': res = max(res, ar[i]//2*2)
        else: res = max(res, ar[i]//2*2-1)
    return res