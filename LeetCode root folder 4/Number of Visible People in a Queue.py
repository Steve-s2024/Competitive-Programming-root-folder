# here is the linear approach: 88%
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0]*n
        stk = []
        for i in range(n-1, -1, -1):
            count = 0
            while stk and stk[-1] < heights[i]:
                stk.pop()
                count += 1
            if stk: count += 1
            ans[i] = count
            stk.append(heights[i])
        # print(ans)
        return ans

# mono-stack and binary search, i think the proper way is to only use mono-stack and have O(n) time: 5%
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        ans = [0]*n
        stk = []
        for i in range(n-1, -1, -1):
            l, r = 0, len(stk)-1
            x = 0
            while l <= r:
                m = (l+r)//2
                if stk[m] > heights[i]:
                    x = m
                    l = m+1
                else: r = m-1

            ans[i] = len(stk)-x
            while stk and stk[-1] < heights[i]: stk.pop()
            stk.append(heights[i])
        # print(ans)
        return ans