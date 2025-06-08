# boring as the previous one, easier though
# cook your dish here
t = int(input())
for tt in range(t):
    n = int(input())
    nums = [int(e) for e in input().split(' ')]
    s = input()

    flag = True
    prev = -float('inf')
    for i in range(n):
        if nums[i] < prev:
            flag = False
            break
        prev = nums[i]

    if flag:
        print(0)
    else:
        hashSet = set(s)
        if len(hashSet) == 1:
            print(-1)
        elif s[0] != s[-1]:
            print(1)
        else:
            copy = nums[:]
            l, r = float('inf'), -float('inf')
            copy.sort()
            for i in range(n):
                if copy[i] != nums[i]:
                    l = min(i, l)
                    r = max(i, r)
            set1 = set(s[:l + 1])
            set2 = set(s[r:])
            comb = set1.union(set2)
            # print(l, r)
            if len(comb) == 2:
                print(1)
            else:
                print(2)


