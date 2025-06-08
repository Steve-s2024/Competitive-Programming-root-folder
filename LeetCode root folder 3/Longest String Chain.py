# reversed, delete one element form word and find the next word accordingly: 61%
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        st = set(words)
        dp = {}

        def recursive(word):
            if word in dp:
                return dp[word]
            res = 0
            for i in range(len(word)):
                tmp = word[:i] + word[i + 1:]
                if tmp in st:
                    res = max(res, recursive(tmp))
            res += 1
            dp[word] = res
            return res

        res = 0
        for i in range(n - 1, -1, -1):
            res = max(recursive(words[i]), res)

        return res


# 5%
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(n):
                a, b = words[i], words[j]
                if len(a) != len(b) - 1:
                    continue

                i1, i2 = 0, 0
                cnt = 0
                while i1 < len(a) and i2 < len(b):
                    if b[i2] != a[i1]:
                        i2 += 1
                        cnt += 1
                    if i2 < len(b) and b[i2] == a[i1]:
                        i1 += 1
                        i2 += 1
                if i1 == len(a) and i2 == len(b) and cnt == 1 or cnt == 0:
                    graph[a].append(b)

        def dfs(node):
            if node in vis:
                return vis[node]
            res = 0
            for nxt in graph[node]:
                res = max(res, dfs(nxt))
            res += 1
            vis[node] = res
            return res

        vis = {}
        res = 0
        for i in range(n):
            res = max(res, dfs(words[i]))

        return res
