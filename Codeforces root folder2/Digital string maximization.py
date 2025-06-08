# optimized solution, use separate array to store the candidates
# for the current digit, the cands can have at most 10 element at a
# time, so removing element from it takes at most 10 time complexity
def solve():
    s = input()
    n = len(s)
    arr = [int(e) for e in list(s)]
    cands = arr[:10]
    i = 10
    res = []
    while cands:
        max_ = -1
        removeIdx = -1
        for idx, cand in enumerate(cands):
            diff = cand - idx
            if diff > max_:
                max_ = diff
                removeIdx = idx
        cands.pop(removeIdx)
        if i < n:
            cands.append(arr[i])
            i+=1
        res.append(str(max_))

    print(''.join(res))

t = int(input())
for tt in range(t):
    solve()


# brute force O(n^2) TLE
def solve():
    s = input()
    n = len(s)
    arr = [int(e) for e in list(s)]
    i = 0
    visited = set()
    res = []
    while len(visited) != n:

        max_ = -1
        idx = -1
        cnt = 0
        j = i
        while j < n:
            if j not in visited:
                diff = arr[j] - cnt
                if diff > max_:
                    max_ = diff
                    idx = j
                cnt += 1
            if cnt == 10:
                break
            j+=1
        visited.add(idx)
        res.append(str(max_))

    print(''.join(res))

t = int(input())
for tt in range(t):
    solve()

