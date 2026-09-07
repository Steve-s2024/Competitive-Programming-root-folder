# the workspace is for any relevant algorithm that is devoted or in relation with to the analysis of
# the following scenario:
#       a histogram with each column made of cube of 1 unit size. each column is formed by cube(s) stacking on each other
#       when the gravity is shifted from downward to leftward, some cubes fall to the left


# 1. the total distance traveled by the falling cubes
# O(nlogn)
def calcDst(nums):

    n = len(nums)
    tp = [(nums[i], i+1) for i in range(n)]
    tp.sort()
    sm = n*(n+1)//2
    ofs = n*(n+1)//2 # ofs is the offset dst which sm overcalculate

    prv = 0
    res = 0
    for i in range(n):
        e, j = tp[i]
        x = e-prv
        res += x*(sm-ofs)

        prv = e
        sm-=j
        ofs-=(n-i)

    return res


print(calcDst([1, 2, 3, 2, 1]))
print(calcDst([5, 4, 1, 1, 1, 1, 3][::-1]))
print(calcDst([1, 2, 3, 4, 5, 6][::-1]))



