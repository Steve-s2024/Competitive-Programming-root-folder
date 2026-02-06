
t = int(input())
for T in range(t):
    [n, x] = [int(e) for e in input().split(' ')]
    skills = [int(e) for e in input().split(' ')]
    skills.sort()
    res = 0
    l, r = len(skills)-1, len(skills)-1
    while l >= 0:
        size = (r - l) + 1
        if skills[l] * size >= x:
            res += 1
            r = l-1
            l = l-1
        else:
            l -= 1
    print(res)
