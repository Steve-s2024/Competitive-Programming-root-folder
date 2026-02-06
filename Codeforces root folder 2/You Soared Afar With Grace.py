# think it is finished, yes it is!! finally.

def solve():
    n = int(input())
    arr = [int(e) for e in input().split(' ')]
    brr = [int(e) for e in input().split(' ')]
    hashSet = set()
    cnt = 0
    flag = True
    for i in range(n):
        a, b = arr[i], brr[i]
        if a == b:
            cnt += 1
        hashSet.add((a, b))
    for i in range(n):
        a, b = arr[i], brr[i]
        if (b, a) not in hashSet:
            flag = False
            break
        hashSet.remove((b, a))
    if n % 2 - cnt < 0:
        flag = False

    if flag:
        res = []
        hashMap = {}
        for i in range(n):
            a, b = arr[i], brr[i]
            hashMap[(a, b)] = i

        for i in range(n//2):
            a, b = arr[i], brr[i]
            i1 = n-1-hashMap[(a, b)]
            i2 = hashMap[(b, a)]
            if a == b:
                i1 = hashMap[(a, b)]
                i2 = n//2
            if i1 != i2:
                res.append((i1+1, i2+1))
                # print(i1, i2)
                key1, key2 = (arr[i1], brr[i1]), (arr[i2], brr[i2])
                arr[i1], brr[i1] = key2[0], key2[1]
                arr[i2], brr[i2] = key1[0], key1[1]
                hashMap[key1] = i2
                hashMap[key2] = i1
        print(len(res))
        for a, b in res:
            print(str(a) + ' ' + str(b))
    else:
        print(-1)


t = int(input())
for tt in range(t):
    solve()

# so close to finish...😢
from collections import defaultdict


def swap(pairs, i, j):
    [a1, b1] = pairs[i]
    [a2, b2] = pairs[j]
    pairs[i] = (a2, b2)
    pairs[j] = (a1, b1)


t = int(input())
for tt in range(t):
    n = int(input())
    perm1 = [int(e) for e in input().split(' ')]
    perm2 = [int(e) for e in input().split(' ')]

    hashMap = defaultdict(int)
    pairs = []
    for i in range(n):
        a, b = perm1[i], perm2[i]
        pairs.append((a, b))
        hashMap[(a, b)] += 1

    visited = set()
    flag = True
    ref = [(-1,-1)] * n
    l, r = 0, n - 1
    for key, val in hashMap.items():
        if key in visited:
            continue

        [a, b] = key
        k1, k2 = key, (b, a)
        v1, v2 = val, hashMap[k2]
        visited.add(k1)
        visited.add(k2)
        if v1 != v2:
            flag = False
            break

        if k1 != k2:
            cnt = v1
            while cnt:
                ref[l] = k1
                ref[r] = k2
                l += 1
                r -= 1
                cnt -= 1
        else:
            cnt = v1
            while cnt > 1:
                ref[l] = k1
                ref[r] = k2
                l+=1
                r-=1
                cnt-=2
            if cnt == 1:
                if n%2 == 0 or ref[n//2] != (-1, -1):
                    flag = False
                    break
                else:
                    ref[n//2] = (a, b)


    # print(ref)
    ans = []
    if flag:
        for i in range(n):
            if ref[i] != pairs[i]:
                ans
    else:
        print(-1)


