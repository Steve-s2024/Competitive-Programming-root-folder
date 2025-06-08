#
def solve():
    s = input()
    res = len(s)
    prev = s[0]
    for c in s:
        a, b = int(prev), int(c)
        if a < b:
            res += a-b
            res += 10
        else:
            res += a-b
        prev = c
    print(res+int(s[-1]))




solve()