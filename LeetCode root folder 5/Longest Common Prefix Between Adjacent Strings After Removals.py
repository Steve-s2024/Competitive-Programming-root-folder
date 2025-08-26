# stupid question!, way too strict on the runtime, the one below hit TLE while this slightly optimized solution passed
class Solution:
    @staticmethod
    def helper(s1, s2):
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]: i += 1
        return i

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        res = 0
        n = len(words)
        minheap = []
        sizes = []
        for i in range(1, n):
            s1, s2 = words[i - 1], words[i]
            size = Solution.helper(s1, s2)
            heapq.heappush(minheap, size)
            if len(minheap) > 3: heapq.heappop(minheap)
            sizes.append(size)
        # print(sizes)
        # print(minheap)
        ans = [0] * n
        for i in range(n):
            a, b = -1, -1
            if i > 0: a = sizes[i - 1]
            if i < n - 1: b = sizes[i]
            mx = 0
            if a != -1 and b != -1: mx = Solution.helper(words[i - 1], words[i + 1])
            for num in minheap:
                if num == a:
                    a = -1
                elif num == b:
                    b = -1
                else:
                    mx = max(mx, num)
            ans[i] = mx
        return ans


# TLE? why?
class Solution:
    @staticmethod
    def helper(s1, s2):
        i = 0
        while i < min(len(s1), len(s2)) and s1[i] == s2[i]: i += 1
        return i

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        maxheap = []
        for i in range(1, n):
            s1, s2 = words[i - 1], words[i]
            heapq.heappush(maxheap, -Solution.helper(s1, s2))

        ans = [0] * n
        for i in range(n):
            a, b = -1, -1
            if i > 0:
                s1, s2 = words[i - 1], words[i]
                a = Solution.helper(s1, s2)
            if i < n - 1:
                s1, s2 = words[i], words[i + 1]
                b = Solution.helper(s1, s2)
            mx = 0
            if i > 0 and i < n - 1:
                mx = Solution.helper(words[i - 1], words[i + 1])
            arr = heapq.nsmallest(3, maxheap)
            for num in arr:
                num = -num
                if num == a:
                    a = -1
                elif num == b:
                    b = -1
                else:
                    mx = max(mx, num)

            ans[i] = mx
        return ans