# insane, this solution relies on the brute force of permutation and partition, which contribute to a factor of
# 24 * 8 * 4 to the overall linear complexity. this is quite the example where you brute force over small inputs
# and combined with linear for big inputs

# look at the four nested loop, it is simply perm -> part -> part[i] -> nums[i], which is 24 * 8 * 4 * n
# around 8 millions in worst case
class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)
        m = len(target)

        def recursive(i):
            if i >= m:
                if stk: par.append(stk[:])
                return
            stk.append(e[i])
            recursive(i+1)
            stk.pop()
            if stk:
                stk[-1] = lcm(stk[-1], e[i])
                recursive(i+1)

        res = inf
        for e in permutations(target):
            stk = []
            par = []
            recursive(0)
            # print(e)
            # print(par)
            for p in par:
                x = 0
                used = set()
                for v in p:
                    mi = v
                    j = -1
                    for i in range(n):
                        re = (v-(nums[i]%v))%v
                        if re < mi and i not in used:
                            mi = re
                            j = i
                    x += mi
                    used.add(j)
                res = min(res, x)

        return res