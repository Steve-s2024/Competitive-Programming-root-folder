# holy fk this is hard, but yet its not hard because of how
# complicated the implementation or question in nature, its just
# you need to be smart to see the details! able to solve it proves
# my improvement
def solve():
    [n, m] = [int(e) for e in input().split(' ')]
    flowers = [int(e) for e in input().split(' ')]
    beauty = [int(e) for e in input().split(' ')]
    i1, i2 = 0, 0
    while i1 < n and i2 < m:
        if flowers[i1] >= beauty[i2]:
            i1+=1
            i2+=1
        else:
            i1+=1
    if i2 == m:
        print(0)
    else:
        # prefix[i] --> the min index to get the first i-th element
        # of beauty in flowers
        prefix = [float('inf')] * m
        suffix = [-float('inf')] * m
        i1, i2 = 0, 0
        while i1 < n and i2 < m:
            if flowers[i1] >= beauty[i2]:
                prefix[i2] = i1
                i1+=1
                i2+=1
            else:
                i1+=1

        i1, i2 = n-1, m-1
        while i1 >= 0 and i2 >= 0:
            if flowers[i1] >= beauty[i2]:
                suffix[i2] = i1
                i1-=1
                i2-=1
            else:
                i1-=1
        # print(prefix, suffix)

        res = float('inf')
        for i in range(m):
            # pretend to eliminate i-th beauty
            if i > 0:
                left = prefix[i-1]
            else:
                left = -1
            if i < m-1:
                right = suffix[i+1]
            else:
                right = n
            if (
                left != float('inf') and
                right != -float('inf') and
                left < right
            ):
                res = min(res, beauty[i])
        if res != float('inf'):
            print(res)
        else:
            print(-1)

t = int(input())
for tt in range(t):
    solve()



# fking hard, even for brute force: TLE
def solve():
    [n, m] = [int(e) for e in input().split(' ')]
    flowers = [int(e) for e in input().split(' ')]
    beauty = [int(e) for e in input().split(' ')]
    i1, i2 = 0, 0
    while i1 < n and i2 < m:
        if flowers[i1] >= beauty[i2]:
            i1+=1
            i2+=1
        else:
            i1+=1
    if i2 == m:
        print(0)
    else:
        res = float('inf')
        for i in range(m):
            i1, i2 = 0, 0
            while i1 < n and i2 < m:
                if i2 == i:
                    i2+=1
                    continue
                while i1 < n:
                    if flowers[i1] >= beauty[i2]:
                        i2+=1
                        i1+=1
                        break
                    i1+=1

            if i2 >= m or (i2 == m-1 and i == m-1):
                res = min(res, beauty[i])
        if res == float('inf'):
            print(-1)
        else:
            print(res)

t = int(input())
for tt in range(t):
    solve()
