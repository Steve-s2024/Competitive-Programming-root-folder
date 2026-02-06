# wtf?????? Q4 is the question lc300 elimination game. I literally wrote a freaking editorial for that not long ago!
# it is a free contest for me. top 100 for first of my life mf!
# with live ranking 71 -> final ranking ~50, i definitely gonna have a delta of at least 60 --> > 2250 new rating


class Solution:
    def lastInteger(self, n: int) -> int:
        l, r = 1, n
        gp = 1
        i = 0
        size = n
        while l <= r:
            # print(l, r)
            if l == r: return l
            if i%2 == 0: r -= gp if size%2 == 0 else 0
            else: l += gp if size%2 == 0 else 0
            gp *= 2
            size -= size//2
            i += 1


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)
        hp = []
        x = 0
        for i in range(n):
            heappush(hp, -nums[i])
            if s[i] == '1': x += -heappop(hp)
        return x


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mp = defaultdict(list)
        for v in nums: mp[v%3].append(v)
        for val in mp.values(): val.sort()
        res = 0
        for ar in[(0, 0, 0), (0, 1, 2), (1, 1, 1), (2, 2, 2)]:
            x = 0
            tp = [mp[i][:] for i in range(3)]
            for v in ar:
                if tp[v]: x += tp[v].pop()
                else: x = -inf

            res = max(res, x)
        return res


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        st = set()
        for i in range(n-1, -1, -1):
            if nums[i] in st: return ceil((i+1)/3)
            st.add(nums[i])
        return 0
