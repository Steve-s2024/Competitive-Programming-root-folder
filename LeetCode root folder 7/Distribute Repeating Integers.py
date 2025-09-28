# awful question, no way to solve
# TLE
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        n = len(quantity)
        frq = Counter(nums)
        vals = list(frq.values())
        m = len(vals)
        arrs = []
        stk = []

        def recursive(mask):
            nonlocal n
            if mask == (1 << n) - 1:
                arrs.append(stk[:])
                return

            for i in range(n):
                if mask & (1 << i) == 0:
                    stk.append(quantity[i])
                    recursive(mask | (1 << i))
                    stk.pop()

        recursive(0)
        # print(arrs)

        for arr in arrs:
            j = 0
            tot = 0
            for i in range(n):
                if vals[j] >= tot + arr[i]:
                    tot += arr[i]
                else:
                    tot = arr[i]
                    j += 1
                while j < m and vals[j] < tot: j += 1
                if j >= m: break
            else:
                # print(vals)
                # print(arr)
                return True
        return False