# not even sure about the solution, I just followed the not so clear instinct, and it worked out...: 18%
# now in retrospective, the solution is very simple yet elegant.
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        mp = defaultdict(list)
        stk = []
        for i in range(n):
            while stk and stk[-1][1] < nums[i]:
                j, e = stk.pop()
                mp[i].append(j)

            stk.append((i, nums[i]))

        # print(mp)
        ans = [-1] * n
        minheap = []
        for i in range(n):
            while minheap and minheap[0][0] < nums[i]:
                e, j = heapq.heappop(minheap)
                ans[j] = nums[i]

            if i in mp:
                for j in mp[i]:
                    heapq.heappush(minheap, (nums[j], j))

        return ans