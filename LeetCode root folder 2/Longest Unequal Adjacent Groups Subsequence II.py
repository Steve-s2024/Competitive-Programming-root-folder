# same dp solution, kindda brute force, didn't expect it to pass: 50%
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                n1, n2 = len(words[i]), len(words[j])
                if groups[i] == groups[j] or n1 != n2:
                    continue
                cnt = 0
                for k in range(n1):
                    if words[i][k] != words[j][k]:
                        cnt += 1
                if cnt == 1:
                    graph[words[i]].append(words[j])
        print(graph)

        dp = {}
        def dfs(node):
            if node in dp:
                return dp[node]
            if not graph[node]:
                return [node]
            max_ = 0
            res = []
            for nextNode in graph[node]:
                tmp = dfs(nextNode)
                if len(tmp) > max_:
                    max_ = len(tmp)
                    res = tmp
            res = [node] + res[:]
            dp[node] = res
            return res

        res = 0
        max_ = 0
        for i in range(n):
            tmp = dfs(words[i])
            if len(tmp) > max_:
                max_ = len(tmp)
                res = tmp
        return res

# awkward, this solution only find the length of the longest
# subsequence that is also valid, but not the subsequence it self
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                n1, n2 = len(words[i]), len(words[j])
                if groups[i] == groups[j] or n1 != n2:
                    continue
                cnt = 0
                for k in range(n1):
                    if words[i][k] != words[j][k]:
                        cnt += 1
                if cnt == 1:
                    graph[words[i]].append(words[j])

        dp = {}
        def dfs(node):
            if node in dp:
                return dp[node]
            if not graph[node]:
                return 0
            maxDepth = 0
            for nextNode in graph[node]:
                maxDepth = max(maxDepth, dfs(nextNode))
            maxDepth += 1
            dp[node] = maxDepth
            return maxDepth

        res = 0
        for i in range(n):
            res = max(res, dfs(words[i]))
        return res+1