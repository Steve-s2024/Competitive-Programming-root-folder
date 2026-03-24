from math import sqrt, ceil

# 2026-02-28

# n*sqrt(q) time complexity for basic mo's algo implementation, the final complexity will be affected by the
# additional code added.
# mo's give optimal block width of n/sqrt(q). which is the BW below.
# the window will behave as left boundary going back and forth inside its block, right point move monotonically to the right
# keep this property in mind when implementing the additional code.

def mo(nums, queries):
    n, q = len(nums), len(queries)

    BCT = ceil(sqrt(q))
    BW = ceil(n / BCT)
    ar = [[] for _ in range(BCT)]

    for i in range(q):
        l, r = queries[i]
        ar[l // BW].append((l, r, i))

    for v in ar: v.sort(key=lambda i: i[1])
    ans = [0] * q

    for i in range(BCT):
        A = ar[i] # the ith block query
        for l, r, j in A:
            ... # do the processing here
    return ans