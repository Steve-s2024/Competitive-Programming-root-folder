# the mono-stack (not exactly, more like the idea behind mono-stack)
# solution, absolutely elegant and extremely hard to conceive.
# : 42%
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        arr = [0]
        cnt = 0
        for i in range(n):
            if hours[i] > 8:
                cnt += 1
            else:
                cnt -= 1
            arr.append(cnt)

        mp = {}
        dp = []
        for i in range(n+1):
            dp.append(0)
            if arr[i]-1 in mp:
                l, r = mp[arr[i]-1], i
                dp[r] = r-l+dp[l]

            if arr[i] not in mp:
                mp[arr[i]] = i

        return max(dp)


# attempting O(n) solution
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        arr = [0]
        cnt = 0
        for i in range(n):
            if hours[i] > 8:
                cnt += 1
            else:
                cnt -= 1
            arr.append(cnt)

        mp = {}
        dp = []
        for i in range(n):
            dp.append(0)
            if arr[i] - 1 in mp:
                l, r = mp[arr[i] - 1], i
                dp[r] = r - l + dp[l]

            if arr[i] not in mp:
                mp[arr[i]] = i

        return max(dp)


# ... how the hell this n^2 even passed lol. brute force with
# hashing and preprocess (without mono-stack): 9754ms, 5%
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        arr = [0]
        cnt = 0
        for i in range(n):
            if hours[i] > 8:
                cnt += 1
            else:
                cnt -= 1
            arr.append(cnt)

        # print(arr)
        res = 0
        for i in range(n+1):
            for j in range(n, i, -1):
                if arr[j] > arr[i]:
                    res = max(res, j-i)
                    break
        return res

