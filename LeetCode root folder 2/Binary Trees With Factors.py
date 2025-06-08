# interesting question, dfs (recursive) solution: 30%
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        hashMap = {}
        for num in arr:
            hashMap[num] = []
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                prod = arr[i] * arr[j]
                if prod in hashMap:
                    hashMap[prod].append((arr[i], arr[j]))

        dp = {}

        def dfs(node):
            if node in dp:
                return dp[node]
            total = 0
            for a, b in hashMap[node]:
                total += dfs(a) * dfs(b)
            dp[node] = total
            return total

        res = 0
        for num in arr:
            if num not in dp:
                res += dfs(num)
        return res