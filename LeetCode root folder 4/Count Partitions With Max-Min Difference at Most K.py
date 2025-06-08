# son of bitch! solved it 5 minutes after the contest ended
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        dp = [0] * n
        dp.append(1)
        maxHeap, minHeap = [], []
        j = n - 1
        mp = defaultdict(int)
        suf = {}
        tot = 1
        suf[n] = tot

        for i in range(n - 1, -1, -1):
            mp[nums[i]] += 1
            heapq.heappush(minHeap, nums[i])
            heapq.heappush(maxHeap, -nums[i])
            mi, mx = minHeap[0], -maxHeap[0]
            while mx - mi > k:
                mp[nums[j]] -= 1
                while mp[minHeap[0]] == 0:
                    heapq.heappop(minHeap)
                while mp[-maxHeap[0]] == 0:
                    heapq.heappop(maxHeap)
                mi, mx = minHeap[0], -maxHeap[0]
                j -= 1

            dp[i] = suf[i + 1] - suf[j + 1] + dp[j + 1]
            tot += dp[i]
            suf[i] = tot

        return dp[0] % MOD





#TLE, have a bad feeling that I will spend the entire contest optimizing this
class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        @cache
        def recursive(i):
            nonlocal n, MOD
            if i >= n:
                return 1
            MX, MI = nums[i], nums[i]
            res = 0
            for j in range(i, n):
                MX, MI = max(nums[j], MX), min(nums[j], MI)
                if MX - MI > k:
                    break
                res += recursive(j+1)
                res %= MOD
            return res
        return recursive(0)
