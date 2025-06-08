# very standard binary search and simulate question: 24%
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # binary search and simulate
        n = len(bloomDay)
        max_ = max(bloomDay)
        min_ = min(bloomDay)
        l, r = min_, max_
        res = -1
        while l <= r:
            mid = (r+l)//2
            # pretend mid as the day
            bouquetCnt = 0
            stack = 0
            for i in range(n):
                if bloomDay[i] <= mid:
                    stack+=1
                else:
                    stack=0
                if stack >= k:
                    stack-=k
                    bouquetCnt+=1
            # print(mid, bouquetCnt)
            if bouquetCnt >= m:
                res = mid
                r = mid-1
            else:
                l = mid+1
        return res