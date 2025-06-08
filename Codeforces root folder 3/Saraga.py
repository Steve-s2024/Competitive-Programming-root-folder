# optimal
def solve():
    s, t = input(), input()
    n = len(s)
    m = len(t)

    prefix = {}
    for i in range(1, n):
        if s[i] not in prefix:
            prefix[s[i]] = i

    suffix = {}
    for i in range(m-2, -1, -1):
        if t[i] not in suffix:
            suffix[t[i]] = i


    minSize = float('inf')
    p = (-1, -1)
    for i in range(26):
        char = chr(i+ord('a'))
        if char in prefix and char in suffix:
            a, b = prefix[char], suffix[char]
            size = a + (m-b)
            if size < minSize:
                minSize = size
                p = (a, b)

    if minSize != float('inf'):
        print(s[:p[0]] + t[p[1]:])
    else:
        print(-1)
t = 1
# t = int(input())
for i in range(t):
    solve()



# passed
def solve():
    s, t = input(), input()
    n = len(s)
    m = len(t)

    mp = {}
    for i in range(m-2, -1, -1):
        if t[i] not in mp:
            mp[t[i]] = i

    res = -1
    for i in range(1, n):
        if s[i] in mp:
            idx = mp[s[i]]
            newSize = i+1 + m-idx-1
            if res == -1 or newSize < len(res):
                res = s[:i + 1] + t[idx + 1:]

    print(res)


t = 1
# t = int(input())
for i in range(t):
    solve()




# TLE


def solve():
    s, t = input(), input()
    n = len(s)
    m = len(t)

    mp = {}
    for i in range(m-2, -1, -1):
        if t[i] not in mp:
            mp[t[i]] = i

    res = -1
    for i in range(1, n):
        if s[i] in mp:
            idx = mp[s[i]]
            tmp = s[:i+1] + t[idx+1:]
            if res == -1 or len(tmp) < len(res):
                res = tmp

    print(res)


t = 1
# t = int(input())
for i in range(t):
    solve()





# finding interesting abbreviation, but not guaranteed the shortest

def solve():
    s, t = input(), input()
    n = len(s)
    m = len(t)
    st = set(t[:m-1]) # get rid of the last character
    for i in range(1, n):
        if s[i] in st:
            for j in range(m-2, -1, -1):
                if t[j] == s[i]:
                    print(s[:i+1] + t[j+1:])
                    break
            else:
                continue
            break
    else:
        print(-1)



t = 1
# t = int(input())
for i in range(t):
    solve()
